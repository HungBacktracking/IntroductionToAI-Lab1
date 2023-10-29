from collections import deque

from implement import *
    
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
    frontier = deque()
    frontier.append(start)
    trace = dict()
    trace[start] = None
    visited = []

    while True:

        # check frontier is empty
        if not frontier:
            raise Exception("No solution found")
        
        # first in, first out
        current = frontier.popleft()
        # print(current.state)

        if(current == end):
            route = []
            while current != None:
                route.append(current)
                current = trace[current]

            route.reverse()
            cost = len(route) - 1

            for bp in bonus_points:
                if (bp[0],bp[1]) in route:
                    cost = cost + bp[2]
            return route,visited,cost     
        
        visited.append(current)

        for neighBor in getNeighbors(current, matrix):
            if neighBor not in frontier and neighBor not in visited:
                # currentNode = Node(state=neighBor, parent=current, cost=current.cost+1)
                frontier.append(neighBor)
                trace[neighBor] = current

    return None, None, -1


if __name__ == '__main__':
    def main(argv):
        in_file = '../input/level_1/input5.txt'
        out_file = '../output/level_1/input5'


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