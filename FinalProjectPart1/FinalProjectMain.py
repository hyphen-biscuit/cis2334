#Dashiell Wendt 2033998

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

class InventoryClass:

	def __init__(self, ManufactureFile, PriceFile, ServiceFile):
		self.manufactureList = [] #lists and dictionaries to hold dat loaded
		self.serviceDateDict = dict()
		self.priceDict = dict() #functionally i dislike the dictionary system but python will python
		self.loaddat(ManufactureFile, PriceFile, ServiceFile)
		print("Loaded")
		self.accessReports()
		print("Opened")

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

	def accessFullInventory(self):
		self.fullInventory = []
		for dat in sorted(self.manufactureList, key=keyGrabManufacture):
			currList = dat[:-1] #create full inventory list and append
			currList.append(self.priceDict[currList[0]])
			currList.append(self.serviceDateDict[currList[0]])
			currList.append(dat[-1])
			self.fullInventory.append(currList)
		with open('FullInventory.csv', 'w') as f:
			for dat in self.fullInventory:
				f.write(strListConversion(dat) + "\n")

	def accessPastServiceInventory(self):
		CurrentDate = datetime.datetime.today()
		filteredInput = []
		for dat in self.fullInventory:
			dateCheck = datetime.datetime.strptime(dat[-2], "%m/%d/%Y")
			if (dateCheck < CurrentDate): # add only late entries
				filteredInput.append(dat)
		with open('PastServiceDateInventory.csv', 'w') as f:
			for dat in sorted(filteredInput, key=keyGrabFilteredNegativeTwo): #the key system only permits a function with one variable. why? because python.
				f.write(strListConversion(dat) + "\n")

	def accessDamagedInventory(self):
		filteredInput = []
		for dat in self.fullInventory:
			if (dat[-1] == "damaged"): # add only if damaged
				filteredInput.append(dat[:-1])
		with open('DamagedInventory.csv', 'w') as f:
			for dat in sorted(filteredInput, key=keyGrabFilteredThree):
				f.write(strListConversion(dat) + "\n") 

	def accessReports(self): #i consider this somewhat gratuitious but have no more efficient method
		self.accessFullInventory()
		self.accessTypeInventory()
		self.accessPastServiceInventory()
		self.accessDamagedInventory()

	def loadPricedatFile(self, PriceFile):
		f = open(PriceFile)
		dat = f.readlines()
		for line in dat:
			splitDat = line.strip().split(',')
			for i in range(len(splitDat)):
				splitDat[i] = int(splitDat[i])
			self.priceDict[splitDat[0]] = splitDat[1]
		f.close()
    
	def loadManufacturedatFile(self, ManufactureFile):
		f = open(ManufactureFile)
		dat = f.readlines()
		for line in dat:
			splitDat = line.strip().split(',')
			splitDat[0] = int(splitDat[0])
			self.manufactureList.append(splitDat)
		f.close()

	def loadServicedatFile(self, ServiceFile):
		f = open(ServiceFile)
		dat = f.readlines()
		for line in dat:
			splitDat = line.strip().split(',')
			splitDat[0] = int(splitDat[0])
			self.serviceDateDict[splitDat[0]] = splitDat[1]
		f.close()

	def loaddat(self, ManufactureFile, PriceFile, ServiceFile):
		self.loadManufacturedatFile(ManufactureFile)
		self.loadPricedatFile(PriceFile)
		self.loadServicedatFile(ServiceFile)

fileNew = InventoryClass("ManufacturerList.csv", "PriceList.csv", "ServiceDatesList.csv") #RUN IT!