from random import randrange
from csv import reader
from sklearn.metrics import confusion_matrix
 
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split


def train_model(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	ps=[]
	rs=[]
	i=1
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		true_neg, false_pos, false_neg, true_pos = confusion_matrix(actual,predicted).ravel()
		precision=true_pos/(true_pos+false_pos)
		recall=true_pos/(true_pos+false_neg)
		accuracy=(true_pos+true_neg)/(true_pos+true_neg+false_pos+false_neg)
		i+=1
		print("Accuracy= ",accuracy)
		print("Precision= ",precision)
		print("Recall= ",recall)
		print("")
		scores.append(accuracy)
		ps.append(precision)
		rs.append(recall)
	return scores,ps,rs

def predict(row, weights,threshold):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= threshold else 0.0


def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	patience=20
	error_so_far=0
	error_sum=0
	for epoch in range(n_epoch):
		if(patience==0):
			break
		if(epoch > 20):
			if(error_so_far>error_sum):
				patience-=1
			else:
				patience=20
		error_so_far=error_sum
		for row in train:
			prediction = predict(row, weights,threshold)
			error = row[-1] - prediction
			error_sum+=error
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
	return weights
 
# Perceptron Algorithm With Stochastic Gradient Descent
def perceptron(train, test, l_rate, n_epoch,threshold):
	predictions = list()
	weights = train_weights(train, l_rate, n_epoch)
	for row in test:
		prediction = predict(row, weights,threshold)
		predictions.append(prediction)
	return(predictions)

def get_dataset(filename, dataset):
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	for i in range(len(dataset[0])):
		for row in dataset:
			row[i] = float(row[i].strip()) 
#######################################################


filename = 'SPECTF.csv'
dataset = list()
get_dataset(filename,dataset)
	
#Parameters
n_folds = 10
l_rate = 0.01
n_epoch = 500
threshold=0.5
print("No_of_folds =", n_folds)
print("Learning rate= ", l_rate)
print("Epochs= ", n_epoch)
print("Threshold", threshold)
print("")


scores,precision,recall = train_model(dataset, perceptron, n_folds, l_rate, n_epoch,threshold)

print("--------------OVERALL--------------")
print('Accuracy: %.3f' % (sum(scores)/float(len(scores))))
print('Precision: %.3f' % (sum(precision)/float(len(precision))))
print('Recall: %.3f' % (sum(recall)/float(len(recall))))