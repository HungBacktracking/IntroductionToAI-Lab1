from collections import deque
from queue import PriorityQueue
import math

from implement import *

control_factor = 0.5

def h_func1(a,b):
    return abs(math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])))

class Node():
    def __init__(self, state, g, h, parent=None):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h 
    
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

def AStar_Lv2(matrix, start, end, bonus_points):
    frontier = PriorityQueue()
    bonus_points_frontiers = dict()
    bonus_points_list = [(i[0], i[1]) for i in bonus_points]
    for bp in bonus_points_list:
        bonus_points_frontiers[bp] = PriorityQueue()

    startNode = Node(state=start, parent=None,  g=0, h=h_func1(start, end))
    frontier.put(startNode)

    if bonus_points_frontiers:
        for bp, bp_frontier in bonus_points_frontiers.items():
            bp_frontier.put(Node(state=start, parent=None,  g=0, h=h_func1(start, bp)))

    visited = []
    last_bn_visited = None

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

            # for bp in bonus_points:
            #     if (bp[0],bp[1]) in route:
            #         cost = cost + bp[2]
            return route,visited,cost 
        
        choices = PriorityQueue()
        # reset = []
        choices.put(current)
        frontier.put(current)
        # reset.append(current)

        for bn_point in bonus_points_list:
            # print()
            if bn_point in bonus_points_frontiers:
                bp_frontier = bonus_points_frontiers[bn_point]
                while not bp_frontier.empty():
                    bp_closet = bp_frontier.get()
                    if bp_closet.state not in visited:
                        # print(str(bp_closet.state) + ": " + str(bp_closet.f))
                        choices.put(bp_closet)
                        # reset.append(bp_closet)
                        bp_frontier.put(bp_closet)
                        break
                # if not flag:
                #     reset.append(-1)

                    
                        
        current = choices.get()
        # print("next: "+ str(current.state) + ": " + str(current.f))

        # if reset[0].state != current.state:
        #     frontier.put(reset[0])

        # for i in range(len(bonus_points)):
        #     if bonus_points[i] in bonus_points_frontiers:
        #         bp_frontier = bonus_points_frontiers[bonus_points[i]]
        #         if reset[i+1].state != current.state:
        #             bp_frontier.put(reset[i+1])
        #         elif current.state == bonus_points[i]:
        #             del bonus_points_frontiers[bonus_points[i]]
        

        # if current.state in bonus_points_list:
        for point in bonus_points:
            if (point[0], point[1]) == current.state:
                print("yes")
                current.f += point[2]
                current.g += point[2]
                if current.state in bonus_points_frontiers:
                    # del bonus_points_frontiers[current.state]
                    bonus_points_list.remove(current.state)
        
        visited.append(current.state)

        for neighBor in getNeighbors(current.state, matrix):
            if neighBor not in visited:
                # print(neighBor)
                nextNode = Node(state=neighBor, parent=current, g=current.g+1, h=h_func1(neighBor, end))
                frontier.put(nextNode)
                if bonus_points_frontiers:
                    for bp, bp_frontier in bonus_points_frontiers.items():
                        # print(bp)
                        bp_frontier.put(Node(state=neighBor, parent=current, g=current.g+1, h=h_func1(neighBor, bp)))

    return None, None, -1

