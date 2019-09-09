#genetic algorithm
import random
import csv
import naive
import pandas


def get_cr_len(filename):
	with open(filename,"r") as csvFile:
		csvReader = csv.reader(csvFile)

		for row in csvReader:
			cr_len = len(row)-1
			break

	return cr_len


# def read_csv(filename, arr):
# 	fields =[]
# 	records =[]
# 	with open(filename,"r") as csvFile:
# 		csvReader = csv.reader(csvFile)
		

# 		for row in csvReader:
# 			records.append(int(row[i]) for i in sel_col)
# 			print(int(row[i]) for i in sel_col)


# 	fields = records[0]
# 	records = records[1:]

# 	return records

def read_csv(filename, arr):
	fields =[]
	records =[]
	sel_col = [0]

	for i in range(len(arr)):
		if (arr[i]==1):
			sel_col.append(i+1)

	with open(filename,"r") as csvFile:
		csvReader = csv.reader(csvFile)

		for row in csvReader:
			records.append(row)


	fields = records[0]
	records = records[1:]
	sel_records = []
	for row in records:
		sel_records.append([row[i] for i in sel_col])

	return sel_records



class individual:
	filename = ""
	def __init__(self, cr_len):
		self.chromosome = []
		self.fitness = 0
		for i in range(cr_len):
			self.chromosome.append(random.randint(1,10)%2)
			

	def crossover(self, other):
		offsprings = []
		for i in range(4):
			offsprings.append(individual(len(self.chromosome)))

		for i in range((len(self.chromosome))):
			for j in range(4):
				if random.randint(1,10)%2==0:
					offsprings[j].chromosome[i] = self.chromosome[i]

				else:
					offsprings[j].chromosome[i] = self.chromosome[i]


		for i in range(4):
			offsprings[i].eval_fitness()

		return offsprings

	def eval_fitness(self):
		records = read_csv(individual.filename, self.chromosome)
		fold_size = int(len(records)/10)+1
		accuracy = []
		#10 fold cross validation
		for i in range(0,len(records),fold_size):
			#getting train and test data
			train, test = naive.getTrainandTest(i, fold_size, records)

			#predicted prior probabilities
			probability_matrix, y_probabilities = naive.getProbabilities(train)

			#getting predicted values
			predicted_values = naive.getPredictions(probability_matrix, test, y_probabilities)

			#getting accuracy
			accuracy.append(naive.getAccuracy(predicted_values, test))

		#printing accuracy values
		self.fitness = (sum(accuracy)/len(accuracy))

	def __lt__(self, other):
		if(self.fitness > other.fitness):
			return True

		return False



class population:
	def __init__(self, pop_size, cr_len, elite_percent, num_of_gen, crossover_rate):
		self.individuals = []
		self.pop_size = pop_size
		self.elite_percent = elite_percent
		self.num_of_gen = num_of_gen
		self.crossover_rate = crossover_rate
		for i in range(pop_size):
			instance = individual(cr_len)
			instance.eval_fitness()
			self.individuals.append(instance)


		for i in range(num_of_gen):
			self.generation()
			print("Generation ",i+1, " fitness: ", self.individuals[pop_size-1].fitness)

		print("Final accuracy obtained: ")
		print(self.individuals[pop_size-1].fitness)


	# def print_indi():
	# 	sort(individuals)

	# 	for i in individuals:
	# 		print(i)
			

	def select_parents(self):
		self.individuals.sort()
		parents = []
		while len(parents)<(self.pop_size*self.crossover_rate/2):
			type(random.random)
			index1 = (random.randint(1,10))%self.pop_size
			index2 = (random.randint(1,10))%self.pop_size
			p1 = self.individuals[index1]
			p2 = self.individuals[index2]
			if index1!=index2 :#and index1>(self.pop_size/self.elite_percent) and index2>(self.pop_size/self.elite_percent):
				pair = [p1, p2]
				chk = 0
				for i in parents:
					if pair==i:
						chk = 1
						break

				if chk==0:
					parents.append(pair)
		
		return parents


	def generation(self):
		parents = self.select_parents()
		for i in parents:
			#chi
			self.individuals = self.individuals+(i[0].crossover(i[1]))

		self.individuals.sort()

		self.individuals = self.individuals[:self.pop_size]
		#print(len(self.individuals))


def main():
	filename = "SPECT.csv"
	individual.filename = filename
	cr_len = get_cr_len(filename)
	pop = population(30, cr_len, 10, 30, 0.5)


if __name__ == '__main__':
	main()


		
