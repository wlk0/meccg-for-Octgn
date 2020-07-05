import collections
import clr
clr.AddReference('System.Web.Extensions')
from System.Web.Script.Serialization import JavaScriptSerializer as json #since .net 3.5?

def deserializePile(pileData, group, who = me):
	mute()

	if pileData is None or len(pileData) == 0:
		return
	if who != me and group.controller != me:
		remoteCall(who, "deserializePile", [pileData, group, who])
	else:
		for c in pileData:
			try:
				card = group.create(c['model'])
			except:
				if (c.Key=="model"):
					card = group.create(c.Value)

def deserializeCard(cardData, who = me):
	mute()
	if who != me:
		remoteCall(who, "deserializeCard", [cardData, who])
	else:
		card = table.create(cardData['model'], cardData['position'][0], cardData['position'][1], 1, True)
		if 'isFaceUp' in cardData and cardData['isFaceUp'] is not None:
			card.isFaceUp = cardData['isFaceUp']
		if 'orientation' in cardData:
			card.orientation = cardData['orientation']
		if 'markers' in cardData and cardData['markers'] is not None:
			for key, qty in {(i['name'], i['model']): i['qty'] for i in cardData['markers']}.items():
				card.markers[key] = qty

def findPlayer(name):
	for p in players:
		if p.name == name:
			return p
	return None

def deserializePlayer(plData):
	if plData is None or len(plData) == 0:
		return

	player = findPlayer(plData['name'])	
	if player is None:
		notify("Warning: player '{}' is not at the table".format(plData['name']))
		return

	if plData['inverted'] is not None and plData['inverted'] != player.isInverted:
		notify("Warning: player '{}' is on the wrong side of the table".format(player.name))

	for cardData in plData['table']:
		deserializeCard(cardData, player)

	if plData['piles'] is not None and len(plData['piles']) > 0:
		for k in plData['piles'].Keys:
			if k not in player.piles:
				continue
			deserializePile(plData['piles'][k], player.piles[k], player)

def serializeCard(card):
	cardData = {}
	cardData['model'] = card.model
	cardData['position'] = card.position
	cardData['isFaceUp'] = card.isFaceUp

	if card.orientation != 0:
		cardData['orientation'] = card.orientation

	if len(card.markers) > 0:
		cardData['markers'] = []
		for id in card.markers:
			cardData['markers'].append({'name': id[0], 'model': id[1], 'qty': card.markers[id]})

	return cardData

def serializePlayer(player):
	plData = {'name': None, 'table': [], 'piles': {}}
	plData['name'] = player.name
	plData['inverted'] = player.isInverted

	# loop and retrieve cards from the table
	for card in table:
		if card.owner == player:
			plData['table'].append(serializeCard(card))

	# serialize player's piles
	for k,v in player.piles.items():
		if len(v) > 0:
			plData['piles'].update({k: [serializeCard(c) for c in v]})

	return plData

def saveTable(group, x=0, y=0):
	mute()

	tab = {"players": None}
			
	# loop each player
	tab['players'] = [serializePlayer(pl) for pl in players]

	filename = saveFileDlg('Select the file to save the game state', '', 'All files (*.*)|*.*')
	if filename == None or filename == '':
		return

	with open(filename, 'w+') as f:
		f.write(json().Serialize(tab))

	notify("{} saved table state to {}".format(me,filename))

def loadTable(group, x=0, y=0):	
	mute()

	filename = openFileDlg('Select the file to load the table states', '', 'All files (*.*)|*.*')
	if filename == None or filename == '':
		return

	with open(filename, 'r') as f:
		tab = json().DeserializeObject(f.read())
		
	if tab['players'] is not None and len(tab['players']) > 0:
		for player in tab['players']:
			deserializePlayer(player)

	notify("{} loaded table state from {}".format(me,filename))

