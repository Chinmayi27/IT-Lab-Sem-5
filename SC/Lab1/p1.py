class Instance:
	def __init__(self, instValue):
		self.instValue = instValue
		self.yes = 0
		self.no = 0 

class attributeProbability:
	def __init__(self, attrName, instValues):
		self.attrName = ""
		self.options = []
		for i in instValues:
			options.append(Instance(i))

import csv
filename = "SPECT.csv"
fields =[]
records =[]

with open(filename,"r") as csvFile:
	csvReader = csv.reader(csvFile)

	for row in csvReader:
		records.append(row)


fields = records[0]
records = records[1:]
total_positive = 0
total_negative = 0

for i in records:
	if()

