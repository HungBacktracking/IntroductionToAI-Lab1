import random 
from BFS import *

class Individual(object): 
    ''' 
    Class representing individual in population 
    '''
    def __init__(self, chromosome, start, end, cities, distance_saved): 
        self.chromosome = chromosome 
        self.fitness = self.cal_fitness(start, end, cities, distance_saved) 

    @classmethod
    def mutated_genes(self, randomGnome): 
        ''' 
        create random genes for mutation 
        '''
        
        # Percentage of mutation is 5% in length of gnome
        count = random.randint(0, int(len(randomGnome) / 100 * 5 ) + 1) 
        
        gene = randomGnome.copy()
        for _ in range(count):
            pos1 = random.randint(0, len(randomGnome) - 1)
            pos2 = random.randint(0, len(randomGnome) - 1)
            gene[pos1], gene[pos2] = gene[pos2], gene[pos1]
        return gene 

    @classmethod
    def create_gnome(self, randomGnome): 
        return self.mutated_genes(randomGnome)

    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring 
        '''
        # chromosome for offspring 
        child_chromosome = [] 

        # position separate from parents
        pos = random.randint(1, max(1, len(self.chromosome) - 1))

        # random probability
        prob = random.random()
        if prob < 0.45:
            child_chromosome = self.chromosome[pos:]
            for val in par2.chromosome:
                if val not in child_chromosome:
                    child_chromosome.append(val)

        elif prob < 0.90:
            child_chromosome = par2.chromosome[pos:]
            for val in self.chromosome:
                if val not in child_chromosome:
                    child_chromosome.append(val)
        
        # insert mutate gene for maintaining diversity 
        elif prob < 0.95:
            child_chromosome = self.mutated_genes(self.chromosome)
        else:
            child_chromosome = self.mutated_genes(par2.chromosome)
       
        return child_chromosome 

    def cal_fitness(self, start, end, cities, distance_saved): 
        ''' 
        Calculate fitness score, it is the cost of TSP path. 
        '''
        if (len(self.chromosome) == 0):
            return distance_saved[start][end]['cost']

        cost = 0
        for i in range(len(self.chromosome)):
            current_city = cities[self.chromosome[i]]
            if i == 0:
                cost += distance_saved[start][current_city]['cost']
                continue
            previous_city = cities[self.chromosome[i - 1]]
            cost += distance_saved[current_city][previous_city]['cost']
        
        last_city = cities[self.chromosome[len(self.chromosome) - 1]]
        cost += distance_saved[last_city][end]['cost']

        return cost


def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def setupCostCities(cities, start, end, matrix):
    distance_saved = {}
    distance_saved[start] = {}
    distance_saved[end] = {}

    route, explored, cost = BFS(matrix, start, end, [])
    distance_saved[start][end] = {}
    distance_saved[start][end]['route'] = route
    distance_saved[start][end]['explored'] = explored
    distance_saved[start][end]['cost'] = cost
    for city in cities:
        distance_saved[city] = {}
        route, explored, cost = BFS(matrix, start, city, [])

        distance_saved[start][city] = {}
        distance_saved[start][city]['route'] = route
        distance_saved[start][city]['explored'] = explored
        distance_saved[start][city]['cost'] = cost

        route, explored, cost = BFS(matrix, city, end, [])

        distance_saved[city][end] = {}
        distance_saved[city][end]['route'] = route
        distance_saved[city][end]['explored'] = explored
        distance_saved[city][end]['cost'] = cost

    for i in range(len(cities)):
        for j in range(len(cities)):
            if i == j:
                 continue
            first = cities[i]
            second = cities[j]
            route, explored, cost = BFS(matrix, first, second, [])

            distance_saved[first][second] = {}
            distance_saved[first][second]['route'] = route
            distance_saved[first][second]['explored'] = explored
            distance_saved[first][second]['cost'] = cost
    
    return distance_saved

def getResult(solution, cities, distance_saved, start, end, cost):
    if (len(cities) == 0):
        return distance_saved[start][end]['route'], distance_saved[start][end]['explored'], distance_saved[start][end]['cost']

    route = []
    visited = []
    for i in range(len(solution)):
        current_city = cities[solution[i]]
        if i == 0:
            for cell in distance_saved[start][current_city]['route']:
                route.append(cell)
            continue
        previous_city = cities[solution[i - 1]]
        for cell in distance_saved[previous_city][current_city]['route']:
                route.append(cell)
    
    last_city = cities[solution[len(solution) - 1]]
    for cell in distance_saved[last_city][end]['route']:
                route.append(cell)

    return route, visited, cost

def GENETIC(matrix, start, end, bonus):
    cities = []
    for val in bonus:
        cities.append((val[0], val[1]))
    distance_saved = setupCostCities(cities, start, end, matrix)

    if (len(cities) == 0):
        return distance_saved[start][end]['route'], distance_saved[start][end]['explored'], distance_saved[start][end]['cost']
    
    # Number of individuals in each generation and number of maximum generation
    POPULATION_SIZE = 100
    MAX_GENERATION = 1000

    # Current generation 
    generation = 0

    # Create initial population 
    population = [] 
    randomGnome = randomSolution(cities)
    for _ in range(POPULATION_SIZE): 
        gnome = Individual.create_gnome(randomGnome) 
        population.append(Individual(gnome, start, end, cities, distance_saved))

    while generation < MAX_GENERATION:
        population = sorted(population, key = lambda x:x.fitness) 
        
        # Init new generation
        new_generation = []

        # 10% of fittest population goes to the next generation 
        num = int((10 * POPULATION_SIZE) / 100) 
        new_generation.extend(population[:num])

        num = int((90 * POPULATION_SIZE) / 100) 
        if generation % 100 == 0 and generation != 0:
            # Each 100 generations, all population will be mutated
            for _ in range(num):
                new_baby = random.choice(population)
                new_baby = Individual.mutated_genes(new_baby.chromosome)
                new_generation.append(Individual(new_baby, start, end, cities, distance_saved))
        else:
            # From 50% of fittest population, Individuals  
            # will mate to produce offspring
            for _ in range(num): 
                parent1 = random.choice(population[:50]) 
                parent2 = random.choice(population[:50]) 
                child = parent1.mate(parent2) 
                new_generation.append(Individual(child, start, end, cities, distance_saved)) 

        population = new_generation 
        generation += 1
    
    population = sorted(population, key = lambda x:x.fitness) 
    print("Generation: {}\tSolution: {}\tFitness: {}".format(generation,population[0].chromosome, population[0].fitness))

    return getResult(population[0].chromosome, cities, distance_saved, start, end, population[0].fitness)