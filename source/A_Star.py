from queue import PriorityQueue
import math

control_factor = 0.5

def h_func1(a,b):
    return abs(math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])))

def h_func2(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

class Node():
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g * (1-control_factor) + h * control_factor
    
    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __le__(self, other):
        return self.f <= other.f

    def __ge__(self, other):
        return self.f >= other.f

    
def getNeighbors(current, matrix):
    dicrections = [[ current[0] -1, current[1]],
                    [ current[0] + 1, current[1]], 
                    [ current[0], current[1] - 1], 
                    [ current[0], current[1] + 1]]    
    neighbors = []
    for r,c in dicrections:
         if 0 <= r < len(matrix)  and 0 <= c  < len(matrix[0]) and matrix[r][c] != 'x':
            neighbors.append((r,c))
    return neighbors

def AStar_heuristic_1(matrix, start, end, bonus_points):
    frontier = PriorityQueue()
    startNode = Node(state=start, parent=None,  g=0, h=0)

    frontier.put(startNode)
    visited = []

    while True:
        if frontier.empty():
            raise Exception("No solution found")
        
        # get lowest f node
        current = frontier.get()
        # print(current.state)

        if current.state in visited:
            continue

        if(current.state == end):
            route = []
            cost = current.g
            while current != None:
                route.append(current.state)
                current = current.parent

            route.reverse()

            for bp in bonus_points:
                if (bp[0],bp[1]) in route:
                    cost = cost + bp[2]
            return route,visited,cost     
        
        visited.append(current.state)

        for neighBor in getNeighbors(current.state, matrix):
            if neighBor not in visited:
                # print(neighBor)
                nextNode = Node(state=neighBor, parent=current, g=current.g+1, h=h_func1(neighBor, end))
                frontier.put(nextNode)

    return None, visited, -1


def AStar_heuristic_2(matrix, start, end, bonus_points):
    frontier = PriorityQueue()
    startNode = Node(state=start, parent=None,  g=0, h=0)

    frontier.put(startNode)
    visited = []

    while True:
        if frontier.empty():
            raise Exception("No solution found")
        
        # get lowest f node
        current = frontier.get()
        # print(current.state)

        if current.state in visited:
            continue

        if(current.state == end):
            route = []
            cost = current.g
            while current != None:
                route.append(current.state)
                current = current.parent

            route.reverse()

            for bp in bonus_points:
                if (bp[0],bp[1]) in route:
                    cost = cost + bp[2]
            return route,visited,cost     
        
        visited.append(current.state)

        for neighBor in getNeighbors(current.state, matrix):
            if neighBor not in visited:
                # print(neighBor)
                nextNode = Node(state=neighBor, parent=current, g=current.g+1, h=h_func2(neighBor, end))
                frontier.put(nextNode)

    return None, visited, -1

