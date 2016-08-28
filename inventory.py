# Comhghall McKeating
# D and D Name Generator
# This class reads the name files and stores them.

from collections import defaultdict

class Inventory:
	namesDict = defaultdict(list)
	dlend_humanCmn = []
	def __init__(self):
		with open("drenlend_human_common.txt", 'r') as file:
			self.dlend_humanCmn = file.readlines()
			self.namesDict['drenlend_human_common'] = self.dlend_humanCmn
			file.close()

	def printNames(self):
		print self.namesDict['drenlend_human_common']

inventory = Inventory()
inventory.printNames()