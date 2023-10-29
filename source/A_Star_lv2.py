# from collections import deque
# import copy
# # from queue import PriorityQueue
# import math

# from implement import *


# def h_func1(a,b):
#     return abs(math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])))

# class Node():
#     def __init__(self, state, parent, g, h):
#         self.state = state
#         self.parent = parent
#         self.g = g
#         self.f = g + h 

# class AStarQueueFrontier():
#     def __init__(self, num_bonus_points=0, bonus_points=None):
#         self.frontier = []
#         self.num_bp = num_bonus_points
#         self.bonus_points = bonus_points
#         # each bonus_point has a frontier
#         self.bonus_frontiers = {} 
#         if bonus_points is not None:
#             for bonus_point in bonus_points:
#                 self.bonus_frontiers[bonus_point] = AStarQueueFrontier()


#     def index_state(self, state):
#         for i in range(len(self.frontier)):
#             if state == self.frontier[i].state:
#                 return i
#         return -1

#     def add(self, node):
#         index = self.index_state(node.state)
#         if index != -1:
#             if self.frontier[index].f > node.f:
#                 del self.frontier[index]
#                 self.frontier.append(node)
#                 self.frontier.sort(key=lambda x:x.f, reverse=True)

#                 if self.num_bp != 0:
#                     for bp in self.bonus_points:
#                         bp_node = Node(state=node.state, parent=node.parent, g=node.g, h= h_func1(node.state, bp))
#                         self.bonus_frontiers[bp].add(bp_node)
#         else:
#             self.frontier.append(node)
#             self.frontier.sort(key=lambda x:x.f, reverse=True)
#             if self.num_bp != 0:
#                 for bp in self.bonus_points:
#                     bp_node = copy.copy(node)
#                     bp_node.f = bp_node.g +  h_func1(node.state, bp)
#                     self.bonus_frontiers[bp].add(bp_node)


#     def empty(self):
#         return len(self.frontier) == 0

#     def remove(self):
#         if self.empty():
#             raise Exception("empty frontier")
#         else:
#             node = self.frontier[-1]
#             if self.num_bp:
#                 closet_bonus_ponits = [(bp, bp_frontier[-1]) for bp, bp_frontier in self.bonus_frontiers.items()]

#                 closet_bp, closet_point = closet_bonus_ponits.sort(key=lambda x:x[1].f, reverse=True)[-1]
#                 if closet_point.f < node.f:
#                     if closet_bp == closet_point.state:
#                         self.bonus_points.remove(closet_bp)
#                         self.num_bp  -= 1
#                     else:
#                         self.bonus_frontiers[closet_bp] =  self.bonus_frontiers[closet_bp][:-1]
                    
#                     index = self.index_state(closet_bp)
#                     if index != -1:
#                             del self.frontier[index]
#                     for frontier in self.bonus_frontiers:
#                         index = self.index_state(closet_bp)
#                         if index != -1:
#                         del self.frontier[index]
#                     return closet_point
#                 else:
#                     next_point = node
#             else:
#                 next_point = node

#                 return node


    
# def getNeighbors(current, matrix):
#     dicrections = [[ current[0] -1, current[1]],
#                     [ current[0] + 1, current[1]], 
#                     [ current[0], current[1] - 1], 
#                     [ current[0], current[1] + 1]]    
#     neighbors = []
#     for r,c in dicrections:
#          if 0 <= r < len(matrix)  and 0 <= c  < len(matrix[0]) and matrix[r][c] != 'x':
#             neighbors.append((r,c))
#     return neighbors

# def AStar(matrix, start, end, bonus_points):
#     frontier = AStarQueueFrontier()
#     startNode = Node(state=start, g=0, parent=None, h=0)
#     frontier.add(startNode)
#     visited = []

#     while True:
#         if frontier.empty():
#             raise Exception("No solution found")
        
#         current = frontier.remove()
#         # print(current.state)

#         if(current.state == end):
#             route = []
#             cost = current.g
#             while current != None:
#                 route.append(current.state)
#                 current = current.parent

#             route.reverse()

#             for bp in bonus_points:
#                 if (bp[0],bp[1]) in route:
#                     cost = cost + bp[2]
#             return route,visited,cost     
        
#         visited.append(current.state)

#         for neighBor in getNeighbors(current.state, matrix):
#             if neighBor not in visited:
#                 # print(neighBor)
#                 nextNode = Node(state=neighBor, parent=current, g=current.g+1, h=h_func1(neighBor, end))
#                 frontier.add(nextNode)

#     return None, None, -1

