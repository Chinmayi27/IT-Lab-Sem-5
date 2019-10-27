import csv
import random

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


def getAccuracy(centres, records, membership_matrix, no_of_records):
    true_positive1 = 0
    true_positive2 = 0

    for i in range(no_of_records):
        result = 1
        if(membership_matrix[i][0]>membership_matrix[i][1]):
            result = 1

        else:
            result = 0

        #print(records[i][0], result)
        if(int(records[i][0])==result):
            #print("%")
            true_positive1 = true_positive1 +1

        else:
            true_positive2 = true_positive2+1

    true_positive2 = true_positive2/no_of_records
    true_positive1 = true_positive1/no_of_records
    return max(true_positive1, true_positive2)





def fuzzyCMeans(c, m, no_of_attr, no_of_iter, records, no_of_records):
    old_centroids = [[random.randrange(0,10) for j in range(no_of_attr)] for i in range(c)]
    new_centroids = [[random.randrange(0,100) for j in range(no_of_attr)] for i in range(c)]

    membership_matrix = [[0 for j in range(c)] for i in range(no_of_records)]

    for num in range(0, no_of_iter):
        #updating membership matrix
        for i in range(0, no_of_records):
            for j in range(0, c):
                temp = 0;
                flag = True
                numer = dist(records[i][1:], old_centroids[j])
                for k in range(0, c):
                     denom = dist(records[i][1:], old_centroids[k])

                     if(denom==0 and dist(records[i][1:], old_centroids[k])==0):
                        if(k==0):
                            membership_matrix[i][0]=1
                            membership_matrix[i][1]=0

                        else:
                            membership_matrix[i][0]=0
                            membership_matrix[i][1]=1

                        flag = False
                        break

                     temp = temp+((numer/denom)**(2/(m-1)))

                if(flag):
                    temp = temp**(-1)
                    membership_matrix[i][j] = temp

        error =0
        for j in range(0, c):
            denom = 0
            numer = [0 for numb in range(no_of_attr)]
            for i in range(0, no_of_records):
                denom = denom+(membership_matrix[i][j]**m)
                numer = vecAdd(numer, scalar((membership_matrix[i][j]**m), records[i][1:]))

            if(denom==0):
                print("d o")
                break

            denom = denom**(-1)
            #print("$#####",denom, numer,"$$$$$")
            new_centroids[j] = scalar(denom, numer)
            if(num%10==0):
                print(new_centroids,"\n\n\n\n\n\n")
            error = vecDiff(new_centroids[j], old_centroids[j])

        old_centroids = new_centroids[::]
        if(error ==0):
            print("Error 0")
            return new_centroids, membership_matrix

    return new_centroids, membership_matrix



def main():
    filename = "SPECTF.csv"
    records = readCSV(filename)

    c = 2
    m = 2
    no_of_iter = 100
    no_of_attr = len(records[0])-1
    no_of_records = len(records)
    centres, membership_matrix = fuzzyCMeans(c, m, no_of_attr, no_of_iter, records, no_of_records)
    print(centres)
    accuracy = getAccuracy(centres, records, membership_matrix, no_of_records)
    print(accuracy)

if __name__ == '__main__':
    main()
