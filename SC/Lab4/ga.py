#genetic algorithm
import random

class individual:
	def __init__(self, cr_len):
		self.chromosome = []
		self.fitness = 0
		for i in range(len):
			chromosome.append(random.random()%2)
			

	def crossover(self, other):
		offsprings = []
		for i in range(4):
			offsprings.append(individual(len(self.chromosome)))

		for i in range((len(self.chromosome))):
			for j in range(4):
				if random.random()%2==0:
					offsprings[j].chromosome[i] = self.chromosome[i]

				else:
					offsprings[j].chromosome[i] = self.chromosome[i]


		for i in range(4):
			offsprings[i].eval_fitness()

		return offsprings

	def eval_fitness(self):


	def __lt__(self, other):
		if(self.fitness < other.fitness):
			return True

		return False



class population:
	def __init__(self, pop_size, cr_len):
		self.individuals = []
		self.pop_size = pop_size
		for i in range(pop_size):
			instance = individual(cr_len)
			instance.eval_fitness()
			individuals.append(instance)


	def print_indi:
		sort(individuals)

		for i in individuals:
			

	def select_parents:
		self.individuals.sort()
		parents = []
		while len(parents)<(pop_size/2):
			p1 = self.individuals[random.random()%pop_size]
			p2 = self.individuals[random.random()%pop_size]
			if p1!=p2 && p1>(self.pop_size/10) && p2(self.pop_size/10)::
				pair = [p1, p2]
				chk = 0
				for i in parents:
					if pair==i:
						chk = 1
						break

				if chk==0:
					parents.append(pair)
		
		return parents


	def generation:
		parents = select_parents()
		for i in parents:
			self.individuals+(i[0].crossover(i[1]))


		self.individuals.sort()

		self.individuals  = self.individuals[:pop_size]

		



