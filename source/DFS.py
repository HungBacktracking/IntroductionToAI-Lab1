def isPointValid(matrix, point):
    if (point[0] < len(matrix) and point[0] >= 0 and point[1] < len(matrix[0]) and point[1] >= 0 and matrix[point[0]][point[1]] != 'x'):
        return True
    return False

def DFS(maze, current, end, bonus_points, explored, trace, directions):
    if end in explored:
        return
    
    explored.append(current)  
    for step in directions:
        next = (current[0] + step[0], current[1] + step[1])
        if next not in explored and isPointValid(maze, next):
            trace[next] = current
            DFS(maze, next, bonus_points, explored, trace, directions)

def DFS_main(maze, start, end, bonus_points):
    explored = []
    dicrections = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    trace = dict()
    trace[start] = None 
    trace[end] = None
    DFS(maze, start, end, bonus_points, explored, trace, dicrections)

    if not trace[end]:
        return None, explored, -1
    
    route = []
    check = end
    while check != start:
        route.append(check)
        check = trace[check]
    route.append(start)
    route.reverse()
    cost = len(route) - 1 # Minus the cost in start point
    for bp in bonus_points:
        if (bp[0], bp[1]) in route:
            cost = cost + bp[2]
    return route, explored, cost   



