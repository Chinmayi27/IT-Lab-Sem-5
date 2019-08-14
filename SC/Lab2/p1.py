import csv
import random 
import copy

def getTrainandTest(pos, fold_size, records):
	test = records[pos:pos+fold_size]
	train = records[:max(0,pos)]+records[pos+fold_size+1:]
	return train, test


def readCSV(filename):
	fields =[]
	records =[]
	with open(filename,"r") as csvFile:
		csvReader = csv.reader(csvFile)

		for row in csvReader:
			records.append(row)


	fields = records[0]
	records = records[1:]

	return records

def intializeWeights(train):
	weights = [0]*(len(train[0])-1)
	for i in range(len(weights)):
		weights[i] = random.random() 

	return weights
def updateWeights(myWeights, row, pred, learning_rate, target):
	diff = pred - target
	for i in range(len(myWeights)):
		myWeights[i] = myWeights[i] + diff*learning_rate*float(row[i+1])

def predict(test, myWeights, threshold):
	predict = []
	for row in test:
		total = 0 
		for i in range(1, len(row)):
			total = total + myWeights[i-1]*float(row[i])

		if(total < threshold):
			predict.append('Iris-setosa')

		else:
			predict.append('Iris-versicolor')

	return predict

def getAccuracy(predicted_values, test):
	total = 0
	for i in range(len(test)):
		total = total + int(not test[i][0]==predicted_values[i])

	return float(total/len(test))


def trainPerceptron(myWeights, max_iterations, train, learning_rate, threshold):
	iter = 1
	error = 100000
	while error!=0 and iter<max_iterations:
		for row in train:
			total = 0
			pred = None

			#sigma w(i)*x(i)
			for j in range(1, len(row)):
				type(row[j])
				total = total + myWeights[j-1]*float(row[j])

			if(total < threshold):
				 pred = 0

			else:
				pred = 1

			updateWeights(myWeights, row, pred, learning_rate, int(not row[0]=='Iris-setosa'))
		if(iter%20==0):
			print(myWeights)
		iter = iter+1



def main():
	print('Single perceptron implementation from scratch')
	filename = "IRIS.csv"
	records = readCSV(filename)

	fold_size = int(len(records)/10)
	accuracy = []
	max_iterations = 200
	weights = intializeWeights(records)
	learning_rate = 0.1
	threshold = 4
	for i in range(0,len(records),fold_size):
		#getting train and test data
		train, test = getTrainandTest(i, fold_size, records)
		myWeights = copy.deepcopy(weights)

		trainPerceptron(myWeights, max_iterations, train, learning_rate, threshold)
		predicted_values = predict(test, myWeights, threshold)
		accuracy.append(getAccuracy(predicted_values, test))

	print(accuracy)

if __name__ == '__main__':
	main()