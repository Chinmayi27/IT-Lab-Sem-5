import csv
import pandas

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

def getProbabilities(records):
	total_positive = 0
	total_negative = 0
	probability_matrix = [[[0 for i in range(2)],[0 for i in range(2)]] for i in range(len(records[0])-1)]
	y_probabilities = [0,0]
	for row in records:
		if(row[0]=='1'):
			total_positive = total_positive+1
			col = 1

		else:
			col = 0
			total_negative = total_negative+1

		for i in range(1,len(row)):
			probability_matrix[i-1][int(row[i])][col] = probability_matrix[i-1][int(row[i])][col]+1

	for i in probability_matrix:
		i[0][0] = float(i[0][0])/total_negative
		i[0][1] = float(i[0][1])/total_positive
		i[1][0] = float(i[1][0])/total_negative
		i[1][1] = float(i[1][1])/total_positive

	y_probabilities[0] = float(total_negative/(total_negative+total_positive))
	y_probabilities[1] = float(total_positive/(total_positive+total_negative))

	return probability_matrix, y_probabilities

def getPredictions(probability_matrix, test, y_probabilities):
	predicted_values =[]
	for row in test:
		prob_yes = 1
		prob_no  = 1
		for i in range(1, len(row)):
			prob_no = prob_no * probability_matrix[i-1][int(row[i])][0]
			prob_yes = prob_yes * probability_matrix[i-1][int(row[i])][1]

		if(prob_yes * y_probabilities[1] > prob_no*y_probabilities[0]):
			predicted_values.append('1')

		else:
			predicted_values.append('0')

	return predicted_values

def getAccuracy(predicted_values, test):
	correct = 0
	for i in range(len(test)):
		#print(predicted_values[i], test[i][0], type(predicted_values[i]), type(test[i][0]))
		if(predicted_values[i] == test[i][0]):
			correct = correct+1

	#print(correct)
	return float(correct/len(test))