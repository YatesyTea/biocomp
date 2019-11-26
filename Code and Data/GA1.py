import random

''' Tuning Levers '''
GENE_LENGTH = 70
POP_SIZE = 50
GENERATIONS = 50
PARENT_SIZE = 5
OFFSPRING_SIZE = 10
MUTATION_RATE = 5


class Population:
    """
        Object list of Individuals
        size is used for loops elsewhere"""

    def __init__(self, individuals):
        self.size = len(individuals)
        self.individuals = individuals
        sort_by_fitness(self.individuals)


def sort_by_fitness(i):
    i.sort(key=lambda x: x.fitness, reverse=True)


''' 
    Randomly generates POP_SIZE individuals 
        for first generation.'''


def generate_first_population():
    individuals = []
    for x in range(0, POP_SIZE):
        individual = generate_individual()
        individuals.append(individual)
    temp_population = Population(individuals)
    return temp_population


''' 
    Runs through a given population and prints
        index, fitness, and gene.'''


def print_population(a):
    for x in range(0, a.size):
        print("Index: {0:03} | Fitness: {1.fitness:03} | Gene: {1.gene} "
              .format(x, a.individuals[x]))


''' 
    Takes a population, returns the highest fitness within.'''


def get_highest_pop_fitness(a):
    highest_fitness = 0
    for x in range(0, a.size):
        if a.individuals[x].fitness > highest_fitness:
            highest_fitness = a.individuals[x].fitness
    return highest_fitness


''' 
    Takes a population, returns the mean fitness within.'''


def get_mean_pop_fitness(a):
    total = 0
    for x in range(0, a.size):
        total += a.individuals[x].fitness
    return total / a.size


def get_highest_fitness_candidate(a):
    value = get_highest_pop_fitness(a)
    for x in range(0, len(a)):
        if a.individuals[x].fitness == value:
            return a.individuals[x]


''' 
    Prints out human readable stats for a given population.'''


def print_stats(a):
    print("Mean Fitness: {0:.2f} | Highest Fitness: {1}".format(get_mean_pop_fitness(a), get_highest_pop_fitness(a)))


''' 
    Uses tournament selection on a given population
        returns a population of OFFSPING_SIZE that
        should hopefully be higher average fitness '''


def tournament_selection(a):
    temp_parents = []
    # Generating a list of potential parents
    for x in range(0, PARENT_SIZE):
        p1 = random.randint(0, a.size - 1)
        p2 = random.randint(0, a.size - 1)

        # Compares the two Individuals and selects the one with higher fitness
        if a.individuals[p1].fitness > a.individuals[p2].fitness:
            temp_parents.append(a.individuals[p1])
        else:
            temp_parents.append(a.individuals[p2])
    parent_pop = Population(temp_parents)
    return parent_pop


class Individual:

    def __init__(self, gene=None, fitness=0):
        if gene is None:
            gene = []
        self.gene = gene
        self.fitness = get_fitness(gene)


'''
    Generates a binary list of GENE_LENGTH length'''


def generate_gene():
    gene = []
    for x in range(0, GENE_LENGTH):
        gene.append(random.randint(1, 2) % 2)
    return gene


'''
    Creates an instance of Individual after using
        generate_gene to create binary list'''


def generate_individual():
    gene = generate_gene()
    individual = Individual(gene, 0)
    return individual


'''
    Returns the fitness of a given gene.
    Is used in the initialisation
        of an instance of Individual'''


def get_fitness(gene):
    fitness = 0
    for x in range(len(gene)):
        if gene[x] == 1:
            fitness += 1
    return fitness


'''
    Input: Instance of Population
    Output: 2 Genes (binary lists)
    Uses 1 point crossover to create
    2 Children '''


def crossover(pop):
    # Initialising empty lists for genes, random selection of parents from list.
    chi1, chi2 = [], []
    par1 = pop.individuals[random.randint(0, pop.size-1)]
    par2 = pop.individuals[random.randint(0, pop.size-1)]
    # Selects a random crossover point.
    point = random.randint(1, GENE_LENGTH - 1)

    # Assigns values up to point from each parent
    for x in range(0, point):
        chi1.append(par1.gene[x])
        chi2.append(par2.gene[x])
    # Assigns values for the other remainder from point to end
    for y in range(point, GENE_LENGTH):
        chi1.append(par2.gene[y])
        chi2.append(par1.gene[y])

    a = Individual(chi1, 0)
    b = Individual(chi2, 0)

    return a, b


'''
    Has a chance by random number gen
        to flip a bit in each location'''


def bitwise_mutation(gene):
    for x in range(0, len(gene)):
        chance = random.randint(1, 100)
        if chance <= MUTATION_RATE:
            gene[x] = (gene[x] + 1) % 2
    return gene


population = generate_first_population()
parents = tournament_selection(population)
offspring = []
a, b = crossover(parents)
a.gene = bitwise_mutation(a.gene)
b.gene = bitwise_mutation(b.gene)

