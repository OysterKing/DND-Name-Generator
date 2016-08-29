# Comhghall McKeating
# D and D Name Generator
# This class reads the name files and stores them.

from collections import defaultdict

class Inventory:
	namesDict = defaultdict(list)
	dlend_humanCmn = []
	def __init__(self):
		with open("drenlend_human_common.txt", 'r') as file:
			self.dlend_humanCmn = file.read().splitlines()
			self.namesDict['drenlend_human_common'] = self.dlend_humanCmn
			file.close()

	def printNames(self, key):
		print self.namesDict[key]

	def addToNameList(self, name, key):
		if key == 'drenlend_human_common':
			if name in self.namesDict[key]:
				print 'Name already exists...'
			else:
				print 'adding name...'
				self.namesDict['drenlend_human_common'].append(name)
				with open("drenlend_human_common.txt", 'a') as file:
					file.write('\n' + name)
					file.close()

inventory = Inventory()
inventory.printNames('drenlend_human_common')
inventory.addToNameList('Borgen', 'drenlend_human_common')
inventory.printNames('drenlend_human_common')