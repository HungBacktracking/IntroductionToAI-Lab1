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
        for j in range(len(cities)):
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

def GENETIC_ALGO(matrix, start, end, bonus):
    cities = []
    for val in bonus:
        cities.append((val[0], val[1]))
    
    distance = setupCostCities(cities, start, end, matrix)
    
    print(distance)