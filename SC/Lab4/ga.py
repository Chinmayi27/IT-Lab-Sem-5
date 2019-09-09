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
		self.fitness = [0,0,0]
		for i in range(cr_len):
			self.chromosome.append(random.randint(1,10)%2)
			

	def crossover(self, other, mutation_rate):
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
			offsprings[i].mutate(mutation_rate)
			offsprings[i].eval_fitness()
			

		return offsprings

	def mutate(self, mutation_rate):
		index1 = 0
		index2 = 0
		if(random.random()<mutation_rate):
			while(index1==index2):
				index1 = (random.randint(0,len(self.chromosome)-1))
				index2 = (random.randint(0,len(self.chromosome)-1))

			temp = self.chromosome[index1]
			self.chromosome[index1] = self.chromosome[index2]
			self.chromosome[index2]  = temp

	def eval_fitness(self):
		records = read_csv(individual.filename, self.chromosome)
		fold_size = int(len(records)/10)+1
		accuracy = []
		precision = []
		recall = []
		ac=0
		prec = 0
		rec = 0
		#10 fold cross validation
		for i in range(0,len(records),fold_size):
			#getting train and test data
			train, test = naive.getTrainandTest(i, fold_size, records)

			#predicted prior probabilities
			probability_matrix, y_probabilities = naive.getProbabilities(train)

			#getting predicted values
			predicted_values = naive.getPredictions(probability_matrix, test, y_probabilities)

			#getting accuracy
			ac, prec, rec =naive.getAccuracy(predicted_values, test)
			accuracy.append(ac)
			precision.append(prec)
			recall.append(rec)

		#printing accuracy values
		self.fitness[0] = (sum(accuracy)/len(accuracy))
		self.fitness[1] = (sum(precision)/len(precision))
		self.fitness[2] = (sum(recall)/len(recall))

	def __lt__(self, other):
		if(self.fitness[0] > other.fitness[0]):
			return True

		return False


class population:
	def __init__(self, pop_size, cr_len, elite_percent, num_of_gen, crossover_rate, mutation_rate):
		self.individuals = []
		self.pop_size = pop_size
		self.elite_percent = elite_percent
		self.num_of_gen = num_of_gen
		self.crossover_rate = crossover_rate
		self.mutation_rate = mutation_rate
		for i in range(pop_size):
			instance = individual(cr_len)
			instance.eval_fitness()
			self.individuals.append(instance)


		for i in range(num_of_gen):
			self.generation()
			print("Generation ",i+1, " fitness: ", self.individuals[pop_size-1].fitness)

		print("Final fitness obtained: ")
		print(self.individuals[pop_size-1].fitness)
		print(self.individuals[pop_size-1].chromosome)
			

	def select_parents(self):
		self.individuals.sort()
		parents = []
		while len(parents)<(self.pop_size*self.crossover_rate/2):
			type(random.random)
			index1 = (random.randint(0,self.pop_size-1))
			index2 = (random.randint(0,self.pop_size-1))
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
			self.individuals = self.individuals+(i[0].crossover(i[1], self.mutation_rate))

		self.individuals.sort()
		self.individuals = self.individuals[:self.pop_size]
		#print(len(self.individuals))


def main():
	filename = "SPECT.csv"
	individual.filename = filename
	cr_len = get_cr_len(filename)
	pop = population(30, cr_len, 10, 30, 0.5, 0.1)


if __name__ == '__main__':
	main()


		
