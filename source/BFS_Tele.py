from queue import Queue

def isPointValid(matrix, point):
    if (point[0] < len(matrix) and point[0] >= 0 and point[1] < len(matrix[0]) and point[1] >= 0 and matrix[point[0]][point[1]] != 'x'):
        return True
    return False

def BFS_Tele(matrix, start, end, teleports):
    path = Queue()
    path.put(start)
    visited = []
    trace = dict()
    trace[start] = None
    dicrections = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    current = (0,0)
    teleports_map = {} 

    for tele in teleports:
        start_tele = (tele[0], tele[1])
        end_tele = (tele[2], tele[3])
        teleports_map[start_tele] = end_tele

    while not path.empty():
        current = path.get()

        if(current == end):
            route = []
            check = end

            while check != start:
                route.append(check)
                check = trace[check]

            route.append(start)
            route.reverse()
            cost = len(route) - 1 # Minus the cost in start point
            for tele in teleports:
                if (tele[0], tele[1]) in route:
                    cost -= 1
            
            return route, visited, cost     

        for dir in dicrections:
            point = (current[0] + dir[0], current[1] + dir[1])

            if isPointValid(matrix = matrix, point = point) and point not in visited:
                trace[point] = current
                visited.append(point)
                path.put(point)
                if point in teleports_map:
                    tele_point = teleports_map[point]
                    trace[tele_point] = point
                    visited.append(tele_point)
                    path.put(tele_point)
                    continue

    return None, None, -1