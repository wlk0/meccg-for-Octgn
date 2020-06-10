# -*- coding: utf-8 -*-

gRegionsMap = {
   'Andrast': {'Type': 'Wilderness', 'Path': ['Andrast Coast', 'Anfalas', 'Bay of Belfalas', 'Eriadoran Coast', 'Old Pûkel-land']},
   'Andrast Coast': {'Type': 'Coastal Seas', 'Path': ['Andrast', 'Bay of Belfalas', 'Eriadoran Coast']},
   'Anduin Vales': {'Type': 'Border-lands', 'Path': ['Brown Lands', 'Grey Mountain Narrows', 'Gundabad', 'High Pass', 'Southern Mirkwood', 'Western Mirkwood', 'Wold & Foothills', 'Woodland Realm']},
   'Anfalas': {'Type': 'Wilderness', 'Path': ['Andrast', 'Bay of Belfalas', 'Belfalas', 'Lamedon', 'Old Pûkel Gap']},
   'Angmar': {'Type': 'Shadow-lands', 'Path': ['Arthedain', 'Forochel', 'Gundabad', 'Rhudaur']},
   'Anórien': {'Type': 'Free-domains', 'Path': ['Ithilien', 'Lebennin', 'Rohan']},
   'Arthedain': {'Type': 'Wilderness', 'Path': ['Angmar', 'Cardolan', 'Forochel', 'Lindon', 'Númeriador', 'Rhudaur', 'The Shire']},
   'Bay of Belfalas': {'Type': 'Coastal Seas', 'Path': ['Andrast Coast', 'Andrast', 'Mouths of the Anduin', 'Anfalas', 'Belfalas']},
   'Belfalas': {'Type': 'Free-domains', 'Path': ['Mouths of the Anduin', 'Anfalas', 'Bay of Belfalas', 'Lamedon', 'Lebennin']},
   'Brown Lands': {'Type': 'Shadow-lands', 'Path': ['Anduin Vales', 'Dagorlad', 'Southern Mirkwood', 'Wold & Foothills']},
   'Cardolan': {'Type': 'Wilderness', 'Path': ['Arthedain', 'Dunland', 'Enedhwaith', 'Eriadoran Coast', 'Hollin', 'Rhudaur', 'The Shire']},
   'Dagorlad': {'Type': 'Shadow-lands', 'Path': ['Brown Lands', 'Horse Plains', 'Ithilien', 'Southern Mirkwood', 'Southern Rhovanion']},
   'Dorwinion': {'Type': 'Border-lands', 'Path': ['Northern Rhovanion', 'Southern Rhovanion']},
   'Dunland': {'Type': 'Wilderness', 'Path': ['Cardolan', 'Enedhwaith', 'Hollin']},
   'Elven Shores': {'Type': 'Coastal Seas', 'Path': ['Eriadoran Coast', 'Lindon']},
   'Enedhwaith': {'Type': 'Wilderness', 'Path': ['Cardolan', 'Dunland', 'Eriadoran Coast', 'Gap of Isen', 'Old Pûkel-land']},
   'Eriadoran Coast': {'Type': 'Coastal Seas', 'Path': ['Andrast', 'Andrast Coast', 'Cardolan', 'Elven Shores', 'Enedhwaith', 'Old Pûkel-land']},
   'Fangorn': {'Type': 'Wilderness', 'Path': ['Gap of Isen', 'Rohan', 'Wold & Foothills']},
   'Forochel': {'Type': 'Wilderness', 'Path': ['Angmar', 'Arthedain', 'Númeriador']},
   'Gap of Isen': {'Type': 'Border-lands', 'Path': ['Enedhwaith', 'Fangorn', 'Old Pûkel-land', 'Rohan']},
   'Gorgoroth': {'Type': 'Dark-domains', 'Path': ['Imlad Morgul', 'Nurn', 'Udûn']},
   'Grey Mountain Narrows': {'Type': 'Shadow-lands', 'Path': ['Anduin Vales', 'Northern Rhovanion', 'Withered Heath', 'Woodland Realm']},
   'Gundabad': {'Type': 'Dark-domains', 'Path': ['Anduin Vales', 'Angmar']},
   'Harondor': {'Type': 'Wilderness', 'Path': ['Mouths of the Anduin', 'Ithilien', 'Khand']},
   'Heart of Mirkwood': {'Type': 'Wilderness', 'Path': ['Northern Rhovanion', 'Southern Mirkwood', 'Southern Rhovanion', 'Western Mirkwood', 'Woodland Realm']},
   'High Pass': {'Type': 'Wilderness', 'Path': ['Anduin Vales', 'Rhudaur']},
   'Hollin': {'Type': 'Wilderness', 'Path': ['Cardolan', 'Dunland', 'Redhorn Gate', 'Rhudaur']},
   'Horse Plains': {'Type': 'Shadow-lands', 'Path': ['Dagorlad', 'Nurn', 'Southern Rhovanion']},
   'Imlad Morgul': {'Type': 'Shadow-lands', 'Path': ['Gorgoroth', 'Ithilien']},
   'Iron Hills': {'Type': 'Wilderness', 'Path': ['Northern Rhovanion', 'Withered Heath']},
   'Ithilien': {'Type': 'Wilderness', 'Path': ['Anórien', 'Dagorlad', 'Harondor', 'Imlad Morgul']},
   'Khand': {'Type': 'Shadow-lands', 'Path': ['Harondor', 'Nurn']},
   'Lamedon': {'Type': 'Border-lands', 'Path': ['Anfalas', 'Belfalas', 'Lebennin']},
   'Lebennin': {'Type': 'Free-domains', 'Path': ['Mouths of the Anduin', 'Anórien', 'Belfalas', 'Lamedon']},
   'Lindon': {'Type': 'Free-domains', 'Path': ['Arthedain', 'Elven Shores', 'Númeriador']},
   'Mouths of the Anduin': {'Type': 'Coastal Seas', 'Path': ['Bay of Belfalas', 'Belfalas', 'Harondor', 'Lebennin']},
   'Northern Rhovanion': {'Type': 'Wilderness', 'Path': ['Dorwinion', 'Heart of Mirkwood', 'Iron Hills', 'Southern Rhovanion', 'Withered Heath', 'Woodland Realm', 'Grey Mountain Narrows']},
   'Nurn': {'Type': 'Dark-domains', 'Path': ['Gorgoroth', 'Horse Plains', 'Khand']},
   'Númeriador': {'Type': 'Wilderness', 'Path': ['Arthedain', 'Forochel', 'Lindon']},
   'Old Pûkel Gap': {'Type': 'Wilderness', 'Path': ['Anfalas', 'Old Pûkel-land']},
   'Old Pûkel-land': {'Type': 'Wilderness', 'Path': ['Andrast', 'Enedhwaith', 'Eriadoran Coast', 'Gap of Isen', 'Old Pûkel Gap']},
   'Redhorn Gate': {'Type': 'Wilderness', 'Path': ['Hollin', 'Wold & Foothills']},
   'Rhudaur': {'Type': 'Wilderness', 'Path': ['Angmar', 'Arthedain', 'Cardolan', 'High Pass', 'Hollin']},
   'Rohan': {'Type': 'Border-lands', 'Path': ['Anórien', 'Fangorn', 'Gap of Isen', 'Wold & Foothills']},
   'Southern Mirkwood': {'Type': 'Dark-domains', 'Path': ['Anduin Vales', 'Brown Lands', 'Dagorlad', 'Heart of Mirkwood', 'Southern Rhovanion', 'Western Mirkwood']},
   'Southern Rhovanion': {'Type': 'Wilderness', 'Path': ['Dagorlad', 'Dorwinion', 'Heart of Mirkwood', 'Horse Plains', 'Northern Rhovanion', 'Southern Mirkwood']},
   'The Shire': {'Type': 'Free-domains', 'Path': ['Arthedain', 'Cardolan']},
   'Udûn': {'Type': 'Dark-domains', 'Path': ['Gorgoroth']},
   'Western Mirkwood': {'Type': 'Wilderness', 'Path': ['Anduin Vales', 'Heart of Mirkwood', 'Southern Mirkwood', 'Woodland Realm']},
   'Withered Heath': {'Type': 'Wilderness', 'Path': ['Iron Hills', 'Northern Rhovanion', 'Grey Mountain Narrows']},
   'Wold & Foothills': {'Type': 'Wilderness', 'Path': ['Anduin Vales', 'Brown Lands', 'Fangorn', 'Redhorn Gate', 'Rohan']},
   'Woodland Realm': {'Type': 'Border-lands', 'Path': ['Anduin Vales', 'Heart of Mirkwood', 'Northern Rhovanion', 'Western Mirkwood', 'Grey Mountain Narrows']},
}

def selectRegion(group, x=0, y=0):
	notify("{} {} {}/{}".format(me,group,x,y))
	notify("board={}".format(table.board))
	notify("boards={}".format(table.boards))
	if table.board != 'promomap':
		table.board = 'promomap'
	else:
		table.board = 'noboard'

def regionWithType(region):
	return "{} ({})".format(region,gRegionsMap[region]['Type'])

def createRegionMapFile(args):
	regionMap = {}
	for id in queryCard({"Type":"Region"},True):
		card = table.create(id,0,0)
		regionMap[card.name] = {}
		regionMap[card.name]['Type'] = card.properties["Region Type"]
		regionMap[card.name]['Path'] = re.split(r',\s?',card.properties["Adjacent Regions"])
		card.delete()
	
	f2 = open("C:\\TEMP\\map.txt", 'w')
	
	for r in sorted (regionMap.keys()):
		line = "   '" + r + "': {'Type': '" +  regionMap[r]['Type'] + "', 'Path': ["
		for p in regionMap[r]['Path']:
			if p != regionMap[r]['Path'][0]: line += ", "
			line += "'" + p + "'" 
		line += "]},\n"
		f2.write(line)
		
	f2.close()
	
def cardArrow(args):
	if args.player != me or not args.targeted: return;
	fromregion = args.fromCard.properties["Region"]
	toregion = args.toCard.properties["Region"]
	if fromregion == "" or toregion == "": return
	path = [fromregion]
	while path[-1] != toregion:
		adjacents = []		
		for r in gRegionsMap[path[-1]]['Path']:
			if not r in path:
				adjacents.append(r)
		if len(adjacents) > 1:
			colors = []
			choices = []
			for r in adjacents: 
				if r == toregion: colors.append('#009900')
				else: colors.append('#000000')
				choices.append(regionWithType(r))
			choice = askChoice("Travel from {} to {} using ?".format(path[-1], toregion), choices, colors)
			if choice == 0: break
			path.append(adjacents[choice-1])
		elif len(adjacents) == 1:
			path.append(adjacents[0])
		else:
			break;

	if path[-1] == toregion:
		nicepath = ""
		for p in path:
			if nicepath != "": nicepath += ", "
			nicepath += regionWithType(p)
		notify("Travel path is: {}".format(nicepath))
	
	