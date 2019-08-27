from random import randrange
from random import random
from csv import reader
from math import exp
from sklearn.metrics import confusion_matrix

def split_dataset(dataset, n_folds):
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

def accuracy_calc(actual, predicted):
	correct = 0
	tn, fp, fn, tp=confusion_matrix(actual,predicted).ravel()
	precision=tp/(tp+fp)
	recall=tp/(tp+fn)
	accuracy=(tp+tn)/(tp+fp+tn+fn)
	return precision,recall,accuracy

def train_model(dataset, algorithm, n_folds, *args):
	folds = split_dataset(dataset, n_folds)
	scores = list()
	prec = list()
	rec = list()
	i=0
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
		accuracy = accuracy_calc(actual, predicted)
		scores.append(accuracy[2])
		prec.append(accuracy[0])
		rec.append(accuracy[1])
		i+=1
		print("Accuracy= ",accuracy[2])
		print("Precision= ",accuracy[0])
		print("Recall= ",accuracy[1])
		
		print("")
	return scores, prec, rec

def activation_function(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activation_function(neuron['weights'], inputs)
			neuron['output'] = 1.0 / (1.0 + exp(-activation))
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs


def backward_prop(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * neuron['output'] * (1.0 - neuron['output'])


def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[-1])] = 1
			backward_prop(network, expected)
			update_weights(network, row, l_rate)

def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network


def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))


def back_propagation(train, test, l_rate, n_epoch, n_hidden):
	n_inputs = len(train[0]) - 1
	n_outputs = len(set([row[-1] for row in train]))
	network = initialize_network(n_inputs, n_hidden, n_outputs)
	train_network(network, train, l_rate, n_epoch, n_outputs)
	predictions = list()
	for row in test:
		prediction = predict(network, row)
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



################################################

filename = 'SPECTF.csv'
dataset = list()

get_dataset(filename, dataset)

#Parameters
n_folds = 10
l_rate = 0.3
n_epoch = 100
n_hidden = 5
print("No_of_folds =", n_folds)
print("Learning rate= ", l_rate)
print("Epochs= ", n_epoch)
print("")


scores,prec, rec = train_model(dataset, back_propagation, n_folds, l_rate, n_epoch, n_hidden)

print("--------------OVERALL--------------")
print('Accuracy: %.7f' % (sum(scores)/float(len(scores))))
print('Precision: %.7f' % (sum(prec)/float(len(prec))))
print('Recall: %.7f' % (sum(rec)/float(len(rec))))