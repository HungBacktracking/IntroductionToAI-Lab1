from queue import PriorityQueue
import math
def h_func1(a,b):
    return abs(math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])))

def h_func2(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

class Node():
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost

def getNeighbors(current, matrix):
    dicrections = [ 
                    [ current[0], current[1] - 1], 
                    [ current[0], current[1] + 1],
                    [ current[0] -1, current[1]],
                    [ current[0] + 1, current[1]],]  
    neighbors = []
    for r,c in dicrections:
         if 0 <= r < len(matrix)  and 0 <= c  < len(matrix[0]) and matrix[r][c] != 'x':
            neighbors.append((r,c))
    return neighbors

def GBFS_heuristic_1(matrix, start, end, bonus_points):
    visited = []
    current = Node(state=start, parent=None, cost=0)
    while True:
        if current.state == end:
            route = []
            cost = current.cost
            while current != None:
                route.append(current.state)
                current = current.parent
            
            route.reverse()

            return route, visited, cost

        visited.append(current.state)
        neighBors = getNeighbors(current.state, matrix)
           
        frontier = PriorityQueue()
        for next in neighBors:
            if next not in visited:
                frontier.put((h_func1(next, end), next))

        if frontier.empty():
            cost = f"GBFS has stopped at ({current.state[0]}, {current.state[1]}). No possible ways found!"
            # print(cost)
            route = []
            while current != None:
                route.append(current.state)
                current = current.parent
            
            route.reverse()
            return route, visited, cost
        
        current = Node(state=frontier.get()[1], parent=current, cost=current.cost+1)
        # print(current.state)
    
    return None, visited, -1

def GBFS_heuristic_2(matrix, start, end, bonus_points):
    visited = []
    current = Node(state=start, parent=None, cost=0)
    while True:
        if current.state == end:
            route = []
            cost = current.cost
            while current != None:
                route.append(current.state)
                current = current.parent
            
            route.reverse()

            return route, visited, cost

        visited.append(current.state)
        neighBors = getNeighbors(current.state, matrix)
           
        frontier = PriorityQueue()
        for next in neighBors:
            if next not in visited:
                frontier.put((h_func2(next, end), next))

        if frontier.empty():
            cost = f"GBFS has stopped at ({current.state[0]}, {current.state[1]}). No possible ways found!"
            # print(cost)
            route = []
            while current != None:
                route.append(current.state)
                current = current.parent
            
            route.reverse()
            return route, visited, cost
        
        current = Node(state=frontier.get()[1], parent=current, cost=current.cost+1)
        # print(current.state)
    
    return None, visited, -1
        
