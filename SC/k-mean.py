import csv
import random
import sys
from statistics import mean

def readCSV(filename):
	fields =[]
	records =[]
	with open(filename,"r") as csvFile:
		csvReader = csv.reader(csvFile)

		for row in csvReader:
			records.append(row)


	fields = records[0]
	records = records[1:]

	for i in range(len(records)):
		for j in range(len(records[0])):
			records[i][j] = float(records[i][j])
	return records

def mean(a):
    return sum(a) / len(a)

def getMean(data):
	avg = [float(sum(col))/len(col) for col in zip(*data)]
	return avg

def dist(arr1, arr2):
    temp_dist = 0
    for i in range(len(arr1)):
        #print(i)
        temp_dist = temp_dist + ((float(arr1[i])-float(arr2[i]))**2)

    temp_dist = temp_dist**(0.5)
    return temp_dist

def kMeans(k, no_of_attr, no_of_iter, records, no_of_records, centres):
	new_centres =[]
	for iter in range(no_of_iter):
		clusters = [[] for i in range(k)]
		#print(clusters)
		#for i in records()
		for i in range(no_of_records):
			distances = []
			mini_dist = 10000000
			cluster = -1
			for j in range(k):
				curr = dist(records[i][1:], centres[j])
				if(curr<mini_dist):
					mini_dist = curr
					cluster = j
			
			#print(cluster)
			clusters[cluster].append(records[i][1:])


		new_centres =[]
		for i in range(k):
			#print(len(clusters[i]), getMean(clusters[i]),"\n\n\n")
			new_centres.append(getMean(clusters[i]))
				
		if(centres==new_centres):
			return new_centres
		
		else:
			centres = new_centres[::]
			#print(centres) 

	return new_centres


def getAccuracy(centres, records, no_of_records):
    true_positive1 = 0
    true_positive2 = 0

    for i in range(no_of_records):
        result = 1
        if(dist(centres[0], records[i])>dist(centres[1], records[i])):
            result = 1

        else:
            result = 0

        if(int(records[i][0])==result):
            true_positive1 = true_positive1 +1

        else:
            true_positive2 = true_positive2+1

    true_positive2 = true_positive2/no_of_records
    true_positive1 = true_positive1/no_of_records
    return max(true_positive1, true_positive2)




def main():
    filename = "SPECTF.csv"
    records = readCSV(filename)
    no_of_records = len(records)
    no_of_iter = 100
    no_of_attr = len(records[0])-1
    k = 2
    centres = []
    indices = []
    while(len(indices)<k):
    	random_index = random.randrange(0,no_of_records)
    	if(random_index not in indices):
    		indices.append(random_index)
    		centres.append(records[random_index][1:])

    #print(centres)
    centres = kMeans(k, no_of_attr, no_of_iter, records, no_of_records, centres)
    accuracy = getAccuracy(centres, records, no_of_records)
    print(accuracy)

if __name__ == '__main__':
    main()
