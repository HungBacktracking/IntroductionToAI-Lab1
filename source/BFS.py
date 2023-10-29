from queue import Queue

def isPointValid(matrix, point):
    if (point[0] < len(matrix) and point[0] >= 0 and point[1] < len(matrix[0]) and point[1] >= 0 and matrix[point[0]][point[1]] != 'x'):
        return True
    return False

def BFS(matrix, start, end, bonus_points):
    path = Queue()
    visited = []
    trace = dict()
    trace[start] = None
    dicrections = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    path.put(start)
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
            for bp in bonus_points:
                if (bp[0], bp[1]) in route:
                    cost = cost + bp[2]
            return route, visited, cost     

        for dir in dicrections:
            point = (current[0] + dir[0], current[1] + dir[1])
            if isPointValid(matrix = matrix, point = point) and point not in visited:
                trace[point] = current
                visited.append(point)
                path.put(point)

    return None, visited, -1