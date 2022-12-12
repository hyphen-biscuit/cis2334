#Dash Wendt

import datetime

        
def keyGrabManufacture(e): # grab list keys, painfully static code but things are fines
    return e[1],e[2];
        
def keyGrabFilteredZero(e):
    return e[0];
        
def keyGrabFilteredNegativeTwo(e):
    return e[-2];
        
def keyGrabFilteredThree(e):
    return e[3];
        
def keyGrabInfo(e):
    return e[3];
        
def strListConversion(datInput): #used for export
    return ','.join([str(elem) for elem in datInput])

class InventoryReports:

	def __init__(self, ManufactureFile, PriceFile, ServiceFile):
		self.manufactureList = [] #lists and dictionaries to hold dat loaded
		self.serviceDateDict = dict()
		self.priceDict = dict() #functionally i dislike the dictionary system but python will python
		self.loaddat(ManufactureFile, PriceFile, ServiceFile)
		print("Loaded")
		self.accessReports()
		print("Opened")

	def loadManufacturedat(self, ManufactureFile):
		f = open(ManufactureFile)
		dat = f.readlines()
		for line in dat:
			splitted = line.strip().split(',')
			splitted[0] = int(splitted[0])
			self.manufactureList.append(splitted)
		f.close()

	def loadPricedat(self, PriceFile):
		f = open(PriceFile)
		dat = f.readlines()
		for line in dat:

			splitted = line.strip().split(',')
			for i in range(len(splitted)):
				splitted[i] = int(splitted[i])
			self.priceDict[splitted[0]] = splitted[1]

		f.close()

	def loadServicedat(self, ServiceFile):
		f = open(ServiceFile)
		dat = f.readlines()
		for line in dat:
			splitted = line.strip().split(',')
			splitted[0] = int(splitted[0])
			self.serviceDateDict[splitted[0]] = splitted[1]

		f.close()

	def loaddat(self, ManufactureFile, PriceFile, ServiceFile):
		self.loadManufacturedat(ManufactureFile)
		self.loadPricedat(PriceFile)
		self.loadServicedat(ServiceFile)

	def accessFullInventory(self):
		self.fullInventory = []
		for dat in sorted(self.manufactureList, key=keyGrabManufacture):
			curr = dat[:-1] #create full inventory list and append
			curr.append(self.priceDict[curr[0]])
			curr.append(self.serviceDateDict[curr[0]])
			curr.append(dat[-1])
			self.fullInventory.append(curr)

		with open('FullInventory.csv', 'w') as f:
			for dat in self.fullInventory:
				f.write(strListConversion(dat) + "\n")

	def accessTypeInventory(self):
		types = set()
		for dat in self.fullInventory:
			types.add(dat[2])

		for typeName in types:
			filteredInput = []
			for dat in self.fullInventory:
				if (dat[2] == typeName):
					copyList = dat[:]
					del copyList[2]
					filteredInput.append(copyList)
			typeName = typeName.capitalize()
			with open(typeName + "Inventory.csv", 'w') as f:
				for dat in sorted(filteredInput, key=keyGrabFilteredZero):
					f.write(strListConversion(dat) + "\n")

	def accessPastServiceInventory(self):
		CurrentDate = datetime.datetime.today()
		filteredInput = []
		for dat in self.fullInventory:
			dateCheck = datetime.datetime.strptime(dat[-2], "%m/%d/%Y")
			if (dateCheck < CurrentDate): # add only late entries
				filteredInput.append(dat)

		with open('PastServiceDateInventory.csv', 'w') as f:
			for dat in sorted(filteredInput, key=keyGrabFilteredNegativeTwo, reverse=True): #the key system only permits a function with one variable. why? because python.
				f.write(strListConversion(dat) + "\n")

	def accessDamagedInventory(self):

		filteredInput = []
		for dat in self.fullInventory:
			if (dat[-1] == "damaged"): # add only if damaged
				filteredInput.append(dat[:-1])

		with open('DamagedInventory.csv', 'w') as f:
			for dat in sorted(filteredInput, key=keyGrabFilteredThree, reverse=True):
				f.write(strListConversion(dat) + "\n")

	def accessReports(self): #i consider this somewhat gratuitious but have no more efficient method
		self.accessFullInventory()
		self.accessTypeInventory()
		self.accessPastServiceInventory()
		self.accessDamagedInventory()

	def interactiveQuery(self):
		QuitBool = True
		CurrentDate = datetime.datetime.today()
		while QuitBool:
			userInput = input("Enter manufacturer and item type or enter Q to exit")
			if (userInput.lower() == 'q'):
				print("Exited")
				QuitBool = False
			else:
				splitted = userInput.split(" ")
				if len(splitted) < 2:
					print("Input must be separated by a space.")
				else:
					splitted = splitted[-2:]
					manufacturer, itemType = splitted[0], splitted[1] #ignore all other entered words
					ItemData = []
					ProductData = []
					for dat in self.fullInventory: #check for make and model against all inventory entries
						serviceDate = datetime.datetime.strptime(dat[-2], "%m/%d/%Y")
						if (dat[2].strip().lower() == itemType.strip().lower()
							and dat[-1] != 'damaged' and serviceDate > CurrentDate):
							if (dat[1].strip().lower() == manufacturer.lower()):
								ItemData.append(dat)
							else:
								ProductData.append(dat)

					if len(ItemData) == 0: # no item match
						print("No such item in inventory")
					else:
						ItemData = sorted(ItemData, key=keyGrabFilteredThree, reverse=True)
						print("\nYour item is:", ItemData[0][0], ItemData[0][1], ItemData[0][2], ItemData[0][3])

						current_min = -1
						if len(ProductData) != 0:
							for i in range(len(ProductData)): #recommend similar
								if (abs(ProductData[i][3] - ItemData[0][3]) < current_min or current_min == -1):
									index = i
									current_min = abs(ProductData[i][3] - ItemData[0][3])
							print("\nYou may, also, consider:", ProductData[index][0], ProductData[index][1], ProductData[index][2], ProductData[index][3], "\n")

fileNew = InventoryReports("ManufacturerList.csv", "PriceList.csv", "ServiceDatesList.csv")
fileNew.interactiveQuery()