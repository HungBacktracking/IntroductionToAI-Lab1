from collections import deque
# from queue import PriorityQueue
import math

from implement import *

control_factor = 0.5

def h_func1(a,b):
    return abs(math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])))

class Node():
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.f = g * (1-control_factor) + h * control_factor

class AStarQueueFrontier():
    def __init__(self):
        self.frontier = []


    def index_state(self, state):
        for i in range(len(self.frontier)):
            if state == self.frontier[i].state:
                return i
        return -1

    def add(self, node):
        index = self.index_state(node.state)
        if index != -1:
            if self.frontier[index].f > node.f:
                del self.frontier[index]
                self.frontier.append(node)
                self.frontier.sort(key=lambda x:x.f, reverse=True)
        else:
            self.frontier.append(node)
            self.frontier.sort(key=lambda x:x.f, reverse=True)


    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    
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

def AStar(matrix, start, end, bonus_points):
    frontier = AStarQueueFrontier()
    startNode = Node(state=start, g=0, parent=None, h=0)
    frontier.add(startNode)
    visited = []

    while True:
        if frontier.empty():
            raise Exception("No solution found")
        
        current = frontier.remove()
        # print(current.state)

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
                frontier.add(nextNode)

    return None, None, -1

