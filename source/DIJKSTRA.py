from queue import PriorityQueue

def isPointValid(matrix, point):
    if (point[0] < len(matrix) and point[0] >= 0 and point[1] < len(matrix[0]) and point[1] >= 0 and matrix[point[0]][point[1]] != 'x'):
        return True
    return False

class Node:
    def __init__(self, position, _weight, _bitmask):
        self.position = position
        self.weight = _weight
        self.bitmask = _bitmask
    
    def __lt__(self, other):
        return self.weight < other.weight
    
def get_weight(point, bonus_points):
    for i in range(len(bonus_points)):
        val = bonus_points[i]
        if point == (val[0], val[1]):
            return val[2] + 1, i
    return 1, -1

def Dijkstra(matrix, start, end, bonus_points):
    INF = 10 ** 10
    mask_size = (1 << 10)

    frontier = PriorityQueue()
    frontier.put(Node(start, 0, 0))

    cost = [[[INF for i in range(mask_size)] for j in range(50)] for k in range(50)]
    trace = [[[None for i in range(mask_size)] for j in range(50)] for k in range(50)]
    cost[start[0]][start[1]][0] = 0

    visited = []
    dicrections = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while not frontier.empty():
        current = frontier.get()
        cur_position = current.position
        cur_weight = current.weight
        cur_bitmask = current.bitmask

        if cur_position not in visited:
            visited.append(cur_position)

        if cur_weight != cost[cur_position[0]][cur_position[1]][cur_bitmask]: 
            continue
        for dir in dicrections:
            point = (cur_position[0] + dir[0], cur_position[1] + dir[1])
            if isPointValid(matrix = matrix, point = point) != True:
                continue

            next_weight, id_bonus = get_weight(point, bonus_points)
            if next_weight <= 0:
                if (cur_bitmask & (1 << id_bonus)) != 0: # Đã đi qua điểm thưởng này rồi, không đi nữa
                    continue
                new_bitmask = (cur_bitmask | (1 << id_bonus))
                if cur_weight + next_weight < cost[point[0]][point[1]][new_bitmask]:
                    trace[point[0]][point[1]][new_bitmask] = cur_position
                    cost[point[0]][point[1]][new_bitmask] = cur_weight + next_weight
                    frontier.put(Node(point, cur_weight + next_weight, new_bitmask))
            else:
                if cur_weight + next_weight < cost[point[0]][point[1]][cur_bitmask]:
                    trace[point[0]][point[1]][cur_bitmask] = cur_position
                    cost[point[0]][point[1]][cur_bitmask] = cur_weight + next_weight
                    frontier.put(Node(point, cur_weight + next_weight, cur_bitmask))

    best_cost = INF
    best_bitmask = -1
    for bitmask in range(0, (1 << 10)):
        if best_cost > cost[end[0]][end[1]][bitmask]:
            best_cost = cost[end[0]][end[1]][bitmask]
            best_bitmask = bitmask

    route = []
    check_pos = end
    check_bitmask = best_bitmask
    while check_pos != start:
        route.append(check_pos)
        weight, id = get_weight(check_pos, bonus_points)
        check_pos = trace[check_pos[0]][check_pos[1]][check_bitmask]
        if id != -1:
            check_bitmask = (check_bitmask ^ (1 << id))

    route.append(start)
    route.reverse()
    
    return route, visited, best_cost