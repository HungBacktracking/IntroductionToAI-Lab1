import random
from BFS import *

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def getCostOfSolution(solution, cities, start, end, distance_saved):
    if (len(cities) == 0):
         return distance_saved[start][end]['cost']

    cost = 0
    for i in range(len(solution)):
        current_city = cities[solution[i]]
        if i == 0:
            cost += distance_saved[start][current_city]['cost']
            continue
        previous_city = cities[solution[i - 1]]
        cost += distance_saved[current_city][previous_city]['cost']
    
    last_city = cities[solution[len(solution) - 1]]
    cost += distance_saved[last_city][end]['cost']

    return cost

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

def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution) - 1):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)

    return neighbours

def getBestNeighbour(cities, start, end, distance_saved, neighbours):
    bestCost = getCostOfSolution(neighbours[0], cities, start, end, distance_saved)
    bestNeighbour = neighbours[0]

    for neighbour in neighbours:
        currentCost = getCostOfSolution(neighbour, cities, start, end, distance_saved)
        if currentCost < bestCost:
            bestCost = currentCost
            bestNeighbour = neighbour
    
    return bestNeighbour, bestCost


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



def HILL_CLIMBING(matrix, start, end, bonus):
    cities = []
    for val in bonus:
        cities.append((val[0], val[1]))
    distance_saved = setupCostCities(cities, start, end, matrix)

    currentSolution = randomSolution(cities)
    currentCost = getCostOfSolution(currentSolution, cities, start, end, distance_saved)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourCost = getBestNeighbour(cities, start, end, distance_saved, neighbours)
    
    while bestNeighbourCost < currentCost:
        currentSolution = bestNeighbour
        currentCost = bestNeighbourCost
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourCost = getBestNeighbour(cities, start, end, distance_saved, neighbours)

    return getResult(currentSolution, cities, distance_saved, start, end, currentCost)
