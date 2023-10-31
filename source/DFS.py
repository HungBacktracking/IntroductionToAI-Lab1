# def isPointValid(matrix, point):
#     if (point[0] < len(matrix) and point[0] >= 0 and point[1] < len(matrix[0]) and point[1] >= 0 and matrix[point[0]][point[1]] != 'x'):
#         return True
#     return False

# def DFS(maze, current, bonus_points, explored, trace, directions):
#     explored.append(current)  
#     for step in directions:
#         next = (current[0] + step[0], current[1] + step[1])
#         if next not in explored and isPointValid(maze, next):
#             trace[next] = current
#             DFS(maze, next, bonus_points, explored, trace, directions)

# def DFS_main(maze, start, end, bonus_points):
#     explored = []
#     dicrections = [[0, 1], [0, -1], [1, 0], [-1, 0]]

#     trace = dict()
#     trace[start] = None 
#     trace[end] = None
#     DFS(maze, start, bonus_points, explored, trace, dicrections)

#     if not trace[end]:
#         return None, explored, -1
    
#     route = []
#     check = end
#     while check != start:
#         route.append(check)
#         check = trace[check]
#     route.append(start)
#     route.reverse()
#     cost = len(route) - 1 # Minus the cost in start point
#     for bp in bonus_points:
#         if (bp[0], bp[1]) in route:
#             cost = cost + bp[2]
#     return route, explored, cost   





from implement import *

class Node():
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
        # for node in self.frontier:
        #  if node.state == state:
        #    return true
        # return false

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
    
def getNeighbors(current, matrix):
    dicrections = [[ current[0] +1, current[1]],
                    [ current[0] - 1, current[1]], 
                    [ current[0], current[1] + 1], 
                    [ current[0], current[1] - 1]]    
    neighbors = []
    for r,c in dicrections:
         if 0 <= r < len(matrix)  and 0 <= c  < len(matrix[0]) and matrix[r][c] != 'x':
            neighbors.append((r,c))
    return neighbors

def DFS_main(matrix, start, end, bonus_points):
    frontier = StackFrontier()
    startNode = Node(state=start, cost=0, parent=None)
    frontier.add(startNode)
    visited = []

    while True:
        if frontier.empty():
            raise Exception("No solution found")
        
        current = frontier.remove()
        # print(current.state)

        if(current.state == end):
            route = []
            cost = current.cost
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
            if not frontier.contains_state(neighBor) and neighBor not in visited:
                currentNode = Node(state=neighBor, parent=current, cost=current.cost+1)
                frontier.add(currentNode)

    return None, None, -1