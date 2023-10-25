import sys, getopt
from implement import *
from BFS import *
from DFS import *
from UCS import *
from GBFS import *
from A_SAO import *

# PATH = './input/level_2/input3.txt'

def main(argv):
    in_file, out_file = './input/', ''
    try:
        opts, argv = getopt.getopt(argv, 'hi:o', ['input=', 'output='])
    except getopt.GetoptError:
        print('Error command')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--input':
            in_file += arg
        elif opt == '--output':
            out_file += arg

    bonus_points, matrix = read_file(in_file)
    start, end = getStartEndPoint(matrix)
    
    out_put = './output/' + out_file + '/bfs/BFS.jpg'
    name = 'BFS'
    route,explored,cost = BFS(matrix,start,end,bonus_points)
    write_cost_path(cost, './output/' + out_file + '/bfs/BFS.txt')
    visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)

    out_put = './output/' + out_file + '/dfs/DFS.jpg'
    name = 'DFS'
    route,explored,cost = DFS(matrix,start,end,bonus_points)
    write_cost_path(cost, './output/' + out_file + '/dfs/DFS.txt')
    visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)

    out_put = './output/' + out_file + '/ucs/UCS.jpg'
    name = 'UCS'
    route,explored,cost = UCS(matrix,start,end,bonus_points)
    write_cost_path(cost, './output/' + out_file + '/ucs/UCS.txt')
    visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)

    out_put = './output/' + out_file + '/gbfs/GBFS.jpg'
    name = 'GBFS'
    route,explored,cost = GBFS(matrix,start,end,bonus_points)
    write_cost_path(cost, './output/' + out_file + '/gbfs/GBFS.txt')
    visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)

    out_put = './output/' + out_file + '/astar/astar.jpg'
    name = 'AStar'
    route,explored,cost = AStar(matrix,start,end,bonus_points)
    write_cost_path(cost, './output/' + out_file + '/astar/astar.txt')
    visualize_maze(matrix,bonus_points,start,end,out_put,name,route,explored)

if __name__ == '__main__':
    main(sys.argv[1:])
