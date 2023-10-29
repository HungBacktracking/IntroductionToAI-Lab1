from collections import deque
# from queue import PriorityQueue

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
    dicrections = [[ current[0] -1, current[1]],
                    [ current[0] + 1, current[1]], 
                    [ current[0], current[1] - 1], 
                    [ current[0], current[1] + 1]]    
    neighbors = []
    for r,c in dicrections:
         if 0 <= r < len(matrix)  and 0 <= c  < len(matrix[0]) and matrix[r][c] != 'x':
            neighbors.append((r,c))
    return neighbors

def BFS(matrix, start, end, bonus_points):
    frontier = QueueFrontier()
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


if __name__ == '__main__':
    def main(argv):
        in_file = './input/level_1/input5.txt'
        out_file = './output/level_1/input5'


        bonus_points, matrix = read_file(in_file)
        start, end = getStartEndPoint(matrix)
        
        # out_put = './output/' + out_file + '/bfs/BFS.jpg'
        # name = 'BFS'
        # route,explored,cost = BFS(matrix,start,end,bonus_points)
        # write_cost_path(cost, './output/' + out_file + '/bfs/BFS.txt')
        # visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)

        # out_put = './output/' + out_file + '/dfs/DFS.jpg'
        # name = 'DFS'
        # route,explored,cost = DFS(matrix,start,end,bonus_points)
        # write_cost_path(cost, './output/' + out_file + '/dfs/DFS.txt')
        # visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)

        out_put = './output/' + out_file + '/bfs/BFS.jpg'
        name = 'BFS'
        route,explored,cost = BFS(matrix,start,end,bonus_points)
        write_cost_path(cost, './output/' + out_file + '/bfs/BFS.txt')
        visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)