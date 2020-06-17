# -*- coding: utf-8 -*-
import re

def gccg2octgnset(set):
	if set == 'TW': return 'The Wizards'
	if set == 'TD': return 'The Dragons'
	if set == 'DM': return 'Dark Minions'
	if set == 'AS': return 'Against the Shadow'
	if set == 'LE': return 'The Lidless Eye'
	if set == 'WH': return 'The White Hand'
	if set == 'BA': return 'The Balrog'
	if set == 'PR': return 'Promotional'
	if set == 'PRde': return 'Promotional german'
	return set

def convertDeck(group, x=0, y=0):
	mute()
	filename = askString("Path to convert (.dck) ?","")
	f = open(filename, 'r')
	f2 = open(filename + ".o8d", 'w')
	whisper("Starting conversion")
	section = ''
	subsection = ''
	f2.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n<deck game="1fe65646-3ee1-4dce-9a60-d33a7c3ce9f2">\n')
	for line in f:
		m = re.match(r'^(Deck|Pool|Sideboard|Sites)$', line)
		if m:
			section = m.group(1)
			if section == 'Pool':
				f2.write('</section>\n<section name="Pool" shared="False">\n')
			elif section == 'Sideboard':
				f2.write('</section>\n<section name="Sideboard" shared="False">\n')
			elif section == 'Sites':
				f2.write('</section>\n<section name="Sites" shared="False">\n')

		m = re.match(r'^# (Hazard|Hero Character|Minion Character|Fallen-wizard Character|Hero Resource|Minion Resource) \(\d+\)$', line)
		if m:
			subsection = m.group(1)			
			if section == 'Deck' and subsection == 'Hazard':
				f2.write('<section name="Hazards" shared="False">\n')
			elif section == 'Deck' and subsection in ['Hero Character','Minion Character','Fallen-wizard Character']:
				f2.write('</section>\n<section name="Characters" shared="False">\n')
			elif section == 'Deck' and subsection in ['Hero Resource','Minion Resource']:
				f2.write('</section>\n<section name="Resources" shared="False">\n')
#			else:
#				whisper("Warning: ignoring section '{}' sub '{}'".format(section, subsection))

		m = re.match(r'^(\d+) (.*) \((.*)\)$', line)
		if m:
			count = m.group(1)
			name = m.group(2)
			ext = m.group(3)
			m2 = re.match(r'(.*) \[\D\]',name)
			if m2: name = m2.group(1)
			found = 0
			for cardid in queryCard({"Name": name},True):
				card = table.create(cardid,0,0)
				if card.set == gccg2octgnset(ext):
					f2.write('<card qty="{}" id="{}">{} ({})</card>\n'.format(count,cardid,cardid,card.set))
					found = found + 1
				else:
					card.delete()
			if not found == 1:
				whisper('Error for {}({}): Found {} card'.format(name,ext,found))

	f2.write('</section><notes>\n<![CDATA[]]>\n</notes></deck>')
	f2.close()
	f.close()
	whisper("Conversion done")
	