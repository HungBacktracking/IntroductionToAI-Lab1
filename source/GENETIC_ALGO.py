import random
from BFS_Tele import *

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def costOfSolution(solution, cities, start, end, distance):
    cost = 0
    for i in range(len(solution)):
        current_city = cities[solution[i]]
        if i == 0:
            cost += distance[start][current_city]['cost']
            continue
        previous_city = cities[solution[i - 1]]
        cost += distance[current_city][previous_city]['cost']
    
    last_city = cities[solution[len(solution) - 1]]
    cost += distance[last_city][end]['cost']

    return cost

def setupCostCities(cities, start, end, matrix):
    distance = {}
    distance[start] = {}
    distance[end] = {}
    for city in cities:
        distance[city] = {}

        first = start
        second = city
        route, explored, cost = BFS_Tele(matrix, first, second, [])

        distance[first][second] = {}
        distance[second][first] = {}
        distance[first][second]['route'] = route
        distance[first][second]['explored'] = explored
        distance[first][second]['cost'] = cost
        distance[second][first]['route'] = route
        distance[second][first]['explored'] = explored
        distance[second][first]['cost'] = cost

        first = end
        route, explored, cost = BFS_Tele(matrix, first, second, [])

        distance[first][second] = {}
        distance[second][first] = {}
        distance[first][second]['route'] = route
        distance[first][second]['explored'] = explored
        distance[first][second]['cost'] = cost
        distance[second][first]['route'] = route
        distance[second][first]['explored'] = explored
        distance[second][first]['cost'] = cost


    for i in range(len(cities) - 1):
        for j in range(i + 1, len(cities)):
            first = cities[i]
            second = cities[j]
            route, explored, cost = BFS_Tele(matrix, first, second, [])

            distance[first][second] = {}
            distance[second][first] = {}
            distance[first][second]['route'] = route
            distance[first][second]['explored'] = explored
            distance[first][second]['cost'] = cost
            distance[second][first]['route'] = route
            distance[second][first]['explored'] = explored
            distance[second][first]['cost'] = cost
    
    return distance

def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution) - 1):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
            
    return neighbours


def GENETIC_ALGO(matrix, start, end, bonus):
    cities = []
    for val in bonus:
        cities.append((val[0], val[1]))
    distance = setupCostCities(cities, start, end, matrix)

    currentSolution = randomSolution(cities)
    neighbours = getNeighbours(currentSolution)

    print(costOfSolution(solution, cities, start, end, distance))
    print()