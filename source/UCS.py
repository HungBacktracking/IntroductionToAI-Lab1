from queue import PriorityQueue

    
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


def UCS(matrix, start, end, bonus_points):
    frontier =  PriorityQueue()
    # startNode = Node(state=start, cost=0, parent=None)
    frontier.put((0, start))
    trace = dict()
    trace[start] = None
    visited = []

    while True:
        if frontier.empty():
            raise Exception("No solution found")
        
        # get the lowest cost in queue()
        current = frontier.get()
        # print(current.state)
        if current[1] in visited:
            continue

        if(current[1] == end):
            route = []
            cost = current[0]
            current = current[1]
            while current != None:
                route.append(current)
                current = trace[current]

            route.reverse()

            for bp in bonus_points:
                if (bp[0],bp[1]) in route:
                    cost = cost + bp[2]
            return route,visited,cost     
        
        visited.append(current[1])

        for neighBor in getNeighbors(current[1], matrix):
            if neighBor not in visited:
                # print(neighBor)
                next = (current[0] + 1, neighBor)
                frontier.put(next)
                trace[neighBor] = current[1]

    return None, visited, -1