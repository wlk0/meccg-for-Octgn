# -*- coding: utf-8 -*-

red_token = ("Red", "00000000-0000-0000-0000-000000000004")
green_token = ("Green", "00000000-0000-0000-0000-000000000005")
blue_token = ("Blue", "00000000-0000-0000-0000-000000000002")

def draw(group, x = 0, y = 0):
	if len(group) == 0: return
	card = group[0]
	card.moveTo(me.hand)

def shuffle(group):
	if len(group) > 0:
		update()
		group.shuffle()

def discard(card, x=0, y=0):
	if card.Type in ['Hero Site','Minion Site','Fallen-wizard Site','Balrog Site','Region'] and card.orientation == Rot0:
		card.moveTo(card.owner.piles['Location Deck'])
	else:
		card.moveTo(card.owner.piles['Discard Pile'])

def playfacedown(card, x=0, y=0):
	card.moveToTable(x,y,True)

def removefromgame(card, x=0, y=0):
	card.delete()

def shufflepileintodeck(group):
	mute()
	for c in group:
		if c.Type in ['Hero Site','Minion Site','Fallen-wizard Site','Balrog Site','Region']:
			c.moveTo(c.owner.piles['Location Deck'])
		else:
			c.moveTo(c.owner.piles['Play Deck'])
	notify("{} returns sites from {} to Location Deck and others cards to Play Deck".format(me, group.name))
	shuffle(me.piles['Play Deck'])

def tapuntap(card, x = 0, y = 0):
	mute()
	if card.orientation == Rot180:
		card.orientation = Rot90
		notify("{} heals '{}'".format(me, card))
	elif card.orientation == Rot90:
		card.orientation = Rot0
		notify("{} untap '{}'".format(me, card))
	else:
		card.orientation = Rot90
		notify("{} tap '{}'".format(me, card))

def woundheal(card, x = 0, y = 0):
	mute()
	if not(isCharacter(card) or isAlly(card) or isAgent(card)): return
	if card.orientation == Rot180:
		card.orientation = Rot90
		notify("{} heals '{}'".format(me, card))
	else:
		card.orientation = Rot180
		notify("{} wounds '{}'".format(me, card))

def untapall(group=table, x = 0, y = 0):
	mute()
	for card in group:
		if card.controller == me and card.orientation == Rot90:
			if not card.Type in ['Hero Site','Minion Site','Fallen-wizard Site','Balrog Site','Region']:
				card.orientation = Rot0
	notify("{} untap all his cards.".format(me))

def flipcard(card, x = 0, y = 0):
	if card.isFaceUp:
		card.isFaceUp = False
	else:
		card.isFaceUp = True

def createCard(group=None, x=0, y=0):
	cardID, quantity = askCard()
	cards = table.create(cardID, x, y, quantity, True)

def createSite(group=None, x=0, y=0):
	notify("{} searches for a site in collection".format(me))
	cardID, quantity = askCard({"Type":["Hero Site","Minion Site","Balrog Site","Fallen-wizard Site"]})
	if cardID != None:
		site = me.piles['Location Deck'].create(cardID, 1)
		site.moveToTable(x,y,True)

def isCharacter(c):
	return c.Type in ['Hero Character','Minion Character','Balrog Character','Fallen-wizard Character']

def isAlly(c):
	return c.Type in ['Hero Resource','Minion Resource','Stage Resource'] and c.properties['Class'].find("Ally") >= 0

def isAgent(c):
	return c.properties['Agent'] == 'yes'

def isWoundable(cards,x=0,y=0):
	for c in cards:
		if not(isCharacter(c) or isAlly(c) or isAgent(c)):
			return False
	return True

def roll2D6(group, x=0, y=0):
	d1 = rnd(1,6)
	d2 = rnd(1,6)
	notify("{} rolls {} ({}+{})".format(me,d1+d2,d1,d2))

def nextphase(group, x=0, y=0):
	if turnNumber() == 0:
		nextTurn()
		setPhase(1)
		return
	phaseName, phaseId = currentPhase()
	if phaseId == 6:
		nextTurn()
		setPhase(1)
	else:
		setPhase(phaseId+1)

def previousphase(group, x=0, y=0):
	if turnNumber() == 0:
		nextTurn()
		setPhase(1)
		return
	phaseName, phaseId = currentPhase()
	if phaseId > 1:
		setPhase(phaseId-1)

def lookAtLocationDeck(group, x = 0, y = 0):
	me.piles['Location Deck'].lookAt(-1, True)

def lookAtSideboard(group, x = 0, y = 0):
	me.piles['Sideboard'].lookAt(-1, True)

def deckLoaded(args):
	if args.player != me: return

	for p in args.groups:
		if p.name == 'Play Deck':
			shuffle(p)

def addRedToken(card, x = 0, y = 0):
	card.markers[red_token] += 1

def subRedToken(card, x = 0, y = 0):
	card.markers[red_token] -= 1

def addGreenToken(card, x = 0, y = 0):
	card.markers[green_token] += 1

def subGreenToken(card, x = 0, y = 0):
	card.markers[green_token] -= 1
	
def addBlueToken(card, x = 0, y = 0):
	card.markers[blue_token] += 1

def subBlueToken(card, x = 0, y = 0):
	card.markers[blue_token] -= 1
