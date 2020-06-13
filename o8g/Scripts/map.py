# -*- coding: utf-8 -*-

gRegionsMap = {
   'Andrast': {'Type': 'W', 'Path': ['Andrast Coast', 'Anfalas', 'Bay of Belfalas', 'Eriadoran Coast', 'Old Pûkel-land']},
   'Andrast Coast': {'Type': 'CS', 'Path': ['Andrast', 'Bay of Belfalas', 'Eriadoran Coast']},
   'Anduin Vales': {'Type': 'BL', 'Path': ['Brown Lands', 'Grey Mountain Narrows', 'Gundabad', 'High Pass', 'Southern Mirkwood', 'Western Mirkwood', 'Wold & Foothills', 'Woodland Realm']},
   'Anfalas': {'Type': 'W', 'Path': ['Andrast', 'Bay of Belfalas', 'Belfalas', 'Lamedon', 'Old Pûkel Gap']},
   'Angmar': {'Type': 'SL', 'Path': ['Arthedain', 'Forochel', 'Gundabad', 'Rhudaur']},
   'Anórien': {'Type': 'FD', 'Path': ['Ithilien', 'Lebennin', 'Rohan']},
   'Arthedain': {'Type': 'W', 'Path': ['Angmar', 'Cardolan', 'Forochel', 'Lindon', 'Númeriador', 'Rhudaur', 'The Shire']},
   'Bay of Belfalas': {'Type': 'CS', 'Path': ['Andrast Coast', 'Andrast', 'Mouths of the Anduin', 'Anfalas', 'Belfalas']},
   'Belfalas': {'Type': 'FD', 'Path': ['Mouths of the Anduin', 'Anfalas', 'Bay of Belfalas', 'Lamedon', 'Lebennin']},
   'Brown Lands': {'Type': 'SL', 'Path': ['Anduin Vales', 'Dagorlad', 'Southern Mirkwood', 'Wold & Foothills']},
   'Cardolan': {'Type': 'W', 'Path': ['Arthedain', 'Dunland', 'Enedhwaith', 'Eriadoran Coast', 'Hollin', 'Rhudaur', 'The Shire']},
   'Dagorlad': {'Type': 'SL', 'Path': ['Brown Lands', 'Horse Plains', 'Ithilien', 'Southern Mirkwood', 'Southern Rhovanion']},
   'Dorwinion': {'Type': 'BL', 'Path': ['Northern Rhovanion', 'Southern Rhovanion']},
   'Dunland': {'Type': 'W', 'Path': ['Cardolan', 'Enedhwaith', 'Hollin']},
   'Elven Shores': {'Type': 'CS', 'Path': ['Eriadoran Coast', 'Lindon']},
   'Enedhwaith': {'Type': 'W', 'Path': ['Cardolan', 'Dunland', 'Eriadoran Coast', 'Gap of Isen', 'Old Pûkel-land']},
   'Eriadoran Coast': {'Type': 'CS', 'Path': ['Andrast', 'Andrast Coast', 'Cardolan', 'Elven Shores', 'Enedhwaith', 'Old Pûkel-land']},
   'Fangorn': {'Type': 'W', 'Path': ['Gap of Isen', 'Rohan', 'Wold & Foothills']},
   'Forochel': {'Type': 'W', 'Path': ['Angmar', 'Arthedain', 'Númeriador']},
   'Gap of Isen': {'Type': 'BL', 'Path': ['Enedhwaith', 'Fangorn', 'Old Pûkel-land', 'Rohan']},
   'Gorgoroth': {'Type': 'DD', 'Path': ['Imlad Morgul', 'Nurn', 'Udûn']},
   'Grey Mountain Narrows': {'Type': 'SL', 'Path': ['Anduin Vales', 'Northern Rhovanion', 'Withered Heath', 'Woodland Realm']},
   'Gundabad': {'Type': 'DD', 'Path': ['Anduin Vales', 'Angmar']},
   'Harondor': {'Type': 'W', 'Path': ['Mouths of the Anduin', 'Ithilien', 'Khand']},
   'Heart of Mirkwood': {'Type': 'W', 'Path': ['Northern Rhovanion', 'Southern Mirkwood', 'Southern Rhovanion', 'Western Mirkwood', 'Woodland Realm']},
   'High Pass': {'Type': 'W', 'Path': ['Anduin Vales', 'Rhudaur']},
   'Hollin': {'Type': 'W', 'Path': ['Cardolan', 'Dunland', 'Redhorn Gate', 'Rhudaur']},
   'Horse Plains': {'Type': 'SL', 'Path': ['Dagorlad', 'Nurn', 'Southern Rhovanion']},
   'Imlad Morgul': {'Type': 'SL', 'Path': ['Gorgoroth', 'Ithilien']},
   'Iron Hills': {'Type': 'W', 'Path': ['Northern Rhovanion', 'Withered Heath']},
   'Ithilien': {'Type': 'W', 'Path': ['Anórien', 'Dagorlad', 'Harondor', 'Imlad Morgul']},
   'Khand': {'Type': 'SL', 'Path': ['Harondor', 'Nurn']},
   'Lamedon': {'Type': 'BL', 'Path': ['Anfalas', 'Belfalas', 'Lebennin']},
   'Lebennin': {'Type': 'FD', 'Path': ['Mouths of the Anduin', 'Anórien', 'Belfalas', 'Lamedon']},
   'Lindon': {'Type': 'FD', 'Path': ['Arthedain', 'Elven Shores', 'Númeriador']},
   'Mouths of the Anduin': {'Type': 'CS', 'Path': ['Bay of Belfalas', 'Belfalas', 'Harondor', 'Lebennin']},
   'Northern Rhovanion': {'Type': 'W', 'Path': ['Dorwinion', 'Heart of Mirkwood', 'Iron Hills', 'Southern Rhovanion', 'Withered Heath', 'Woodland Realm', 'Grey Mountain Narrows']},
   'Nurn': {'Type': 'DD', 'Path': ['Gorgoroth', 'Horse Plains', 'Khand']},
   'Númeriador': {'Type': 'W', 'Path': ['Arthedain', 'Forochel', 'Lindon']},
   'Old Pûkel Gap': {'Type': 'W', 'Path': ['Anfalas', 'Old Pûkel-land']},
   'Old Pûkel-land': {'Type': 'W', 'Path': ['Andrast', 'Enedhwaith', 'Eriadoran Coast', 'Gap of Isen', 'Old Pûkel Gap']},
   'Redhorn Gate': {'Type': 'W', 'Path': ['Hollin', 'Wold & Foothills']},
   'Rhudaur': {'Type': 'W', 'Path': ['Angmar', 'Arthedain', 'Cardolan', 'High Pass', 'Hollin']},
   'Rohan': {'Type': 'BL', 'Path': ['Anórien', 'Fangorn', 'Gap of Isen', 'Wold & Foothills']},
   'Southern Mirkwood': {'Type': 'DD', 'Path': ['Anduin Vales', 'Brown Lands', 'Dagorlad', 'Heart of Mirkwood', 'Southern Rhovanion', 'Western Mirkwood']},
   'Southern Rhovanion': {'Type': 'W', 'Path': ['Dagorlad', 'Dorwinion', 'Heart of Mirkwood', 'Horse Plains', 'Northern Rhovanion', 'Southern Mirkwood']},
   'The Shire': {'Type': 'FD', 'Path': ['Arthedain', 'Cardolan']},
   'Udûn': {'Type': 'DD', 'Path': ['Gorgoroth']},
   'Western Mirkwood': {'Type': 'W', 'Path': ['Anduin Vales', 'Heart of Mirkwood', 'Southern Mirkwood', 'Woodland Realm']},
   'Withered Heath': {'Type': 'W', 'Path': ['Iron Hills', 'Northern Rhovanion', 'Grey Mountain Narrows']},
   'Wold & Foothills': {'Type': 'W', 'Path': ['Anduin Vales', 'Brown Lands', 'Fangorn', 'Redhorn Gate', 'Rohan']},
   'Woodland Realm': {'Type': 'BL', 'Path': ['Anduin Vales', 'Heart of Mirkwood', 'Northern Rhovanion', 'Western Mirkwood', 'Grey Mountain Narrows']},
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
	return region + " [" + gRegionsMap[region]['Type'] + "]"

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

def findshortestpaths(maxdepth, start, goal, paths):
    explored = []
    queue = [[start]]

    if start == goal:
        paths.append([goal])
        return 1

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = gRegionsMap[node]['Path']
            for neighbour in neighbours:
                if not neighbour in path:
                    new_path = list(path)
                    new_path.append(neighbour)
                    if neighbour == goal:
                        paths.append(new_path)
                    elif len(path) < (maxdepth-1):
                         queue.append(new_path)

    if len(paths) > 0:
        return len(paths[0])
        
    return -1

def selectautomatedpath(fromregion, toregion):
	possiblepaths = []
	npaths = findshortestpaths(4, fromregion, toregion, possiblepaths)
	if npaths > 0:
		colors = []
		choices = []
		for p in possiblepaths:
			colors.append('#000000')
			if len(p) > 2: choices.append(pathtostring(p[1:-1]))			
			else: choices.append("<Direct>")
		choice = askChoice("Path between " + regionWithType(fromregion) + " and " + regionWithType(toregion) + " ?", choices, colors)
		if choice == 0: return []
		return possiblepaths[choice-1]
	
	whisper("No path within 4 regions...")
	return []

def selectmanualpath(fromregion, toregion):
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
			choice = askChoice("Next region from {} to {} ?".format(path[-1], toregion), choices, colors)
			if choice == 0: break
			path.append(adjacents[choice-1])
		elif len(adjacents) == 1:
			path.append(adjacents[0])
		else:
			break
	return path

def pathtostring(path):
	nicepath = ""
	for p in path:
		if nicepath != "": nicepath += ", "
		nicepath += regionWithType(p)
	return nicepath

def cardArrow(args):
	if args.player != me or not args.targeted: return
	fromregion = args.fromCard.properties["Region"]
	toregion = args.toCard.properties["Region"]
	if fromregion == "" or toregion == "": return
	
	path = selectautomatedpath(fromregion, toregion)
#	if len(path) == 0:
#		path = selectmanualpath(fromregion, toregion)

	if len(path) > 0 and path[-1] == toregion:
		notify("Travel path is: " + pathtostring(path))
	else:
		args.fromCard.arrow(args.toCard, False)
