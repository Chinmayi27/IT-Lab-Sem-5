import csv
import random
import math
import copy

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


def dist(arr1, arr2):
    temp_dist = 0
    for i in range(len(arr1)):
        temp_dist = temp_dist + ((float(arr1[i])-float(arr2[i]))**2)


    temp_dist = temp_dist**(0.5)

    return temp_dist

def scalar(k, arr1):
    temp_prod=[]
    for i in range(len(arr1)):
        temp_prod.append(float(arr1[i])*k)

    return temp_prod

def vecAdd(arr1, arr2):
    temp_sum = list()
    for i in range(len(arr1)):
        temp_sum.append(float(arr1[i])+float(arr2[i]))

    return temp_sum

def vecDiff(arr1, arr2):
    diff = 0
    for i in range(len(arr1)):
        diff = diff+arr1[i]-arr2[i]

    return diff


def getAccuracy(centres, records, no_of_records):
    true_positive1 = 0
    true_positive2 = 0

    for i in range(no_of_records):
        result = 1
        if(dist(centres[0], records[i])>=dist(centres[1], records[i])):
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





def fuzzyCMeans(c, m, no_of_attr, no_of_iter, records, no_of_records):
    old_centroids = [[random.randrange(0,90) for j in range(no_of_attr)] for i in range(c)]
    new_centroids = [[0 for j in range(no_of_attr)] for i in range(c)]

    membership_matrix = [[0 for j in range(c)] for i in range(no_of_records)]

    for num in range(0, no_of_iter):
        #print(num)
        for i in range(0, no_of_records):

            membership_matrix[i][0] = (1+(dist(records[i][1:], old_centroids[0])/dist(records[i][1:], old_centroids[1]))**(2/(m-1)))**(-1)
            membership_matrix[i][1] = (1+(dist(records[i][1:], old_centroids[1])/dist(records[i][1:], old_centroids[0]))**(2/(m-1)))**(-1)

        error =0
        for j in range(0, c):
            denom = 0
            numer = [0 for numb in range(no_of_attr)]
            for i in range(0, no_of_records):
                denom = denom+(membership_matrix[i][j]**m)
                numer = vecAdd(numer, scalar((membership_matrix[i][j]**m), records[i][1:]))

            if(denom==0):
                denom =1
                break

            denom = denom**(-1)
            new_centroids[j] = scalar(denom, numer)
            for x in new_centroids[j]:
                x = math.floor(x)

            error = vecDiff(new_centroids[j], old_centroids[j])


        old_centroids = copy.deepcopy(new_centroids)

        if(num%10==0):
            print(getAccuracy(old_centroids, records, no_of_records))
        if(error ==0):
            print("Error 0")
            return new_centroids, membership_matrix

    return new_centroids, membership_matrix



def main():
    filename = "SPECTF.csv"
    records = readCSV(filename)

    c = 2
    m = 2
    no_of_iter = 1
    no_of_attr = len(records[0])-1
    no_of_records = len(records)
    centres, membership_matrix = fuzzyCMeans(c, m, no_of_attr, no_of_iter, records, no_of_records)
    accuracy = getAccuracy(centres, records, no_of_records)
    print("Accuracy",accuracy)

if __name__ == '__main__':
    main()
