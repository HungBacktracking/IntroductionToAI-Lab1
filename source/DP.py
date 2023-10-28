from BFS_Tele import *

INF = 10 ** 10
mask_size = (1 << 10)

# Tạo mảng dp với kích thước 11 * mask_size * 2 và giá trị ban đầu là 10^10
dp = [[[INF for i in range(2)] for j in range(mask_size)] for k in range(11)]
path = []

def getCostOfSolution(solution, bonus_points, start, end, distance_saved):
    cost = 0
    for i in range(len(solution)):
        tmp = bonus_points[solution[i]]
        current_point = (tmp[0], tmp[1])
        if i == 0:
            cost += distance_saved[start][current_point]['cost']
            continue
        tmp = bonus_points[solution[i - 1]]
        previous_point = (tmp[0], tmp[1])
        cost += distance_saved[current_point][previous_point]['cost']
    
    tmp = bonus_points[solution[len(solution) - 1]]
    last_point = (tmp[0], tmp[1])
    cost += distance_saved[last_point][end]['cost']

    return cost

def setupCostVisitBonusPoint(bonus_points, start, end, matrix):
    distance_saved = {}
    distance_saved[start] = {}
    distance_saved[end] = {}

    route, explored, cost = BFS_Tele(matrix, start, end, [])
    distance_saved[start][end] = {}
    distance_saved[start][end]['route'] = route
    distance_saved[start][end]['explored'] = explored
    distance_saved[start][end]['cost'] = cost

    for val in bonus_points:
        point = (val[0], val[1])
        distance_saved[point] = {}
        route, explored, cost = BFS_Tele(matrix, start, point, [])

        distance_saved[start][point] = {}
        distance_saved[start][point]['route'] = route
        distance_saved[start][point]['explored'] = explored
        distance_saved[start][point]['cost'] = cost

        route, explored, cost = BFS_Tele(matrix, point, end, [])

        distance_saved[point][end] = {}
        distance_saved[point][end]['route'] = route
        distance_saved[point][end]['explored'] = explored
        distance_saved[point][end]['cost'] = cost

    for i in range(len(bonus_points)):
        for j in range(len(bonus_points)):
            if i == j:
                 continue
            first_point = bonus_points[i]
            second_point = bonus_points[j]
            first = (first_point[0], first_point[1])
            second = (second_point[0], second_point[1])
            route, explored, cost = BFS_Tele(matrix, first, second, [])

            distance_saved[first][second] = {}
            distance_saved[first][second]['route'] = route
            distance_saved[first][second]['explored'] = explored
            distance_saved[first][second]['cost'] = cost
    
    return distance_saved

def reset():
    for i in range(10):
            for j in range(mask_size):
                dp[i][j][0], dp[i][j][1] = INF, INF

def getResult(solution, bonus_points, distance_saved, start, end, cost):
    route = []
    visited = []
    for i in range(len(solution)):
        tmp = bonus_points[solution[i]]
        current_point = (tmp[0], tmp[1])
        if i == 0:
            for cell in distance_saved[start][current_point]['route']:
                route.append(cell)
            continue
        tmp = bonus_points[solution[i - 1]]
        previous_point = (tmp[0], tmp[1])
        for cell in distance_saved[previous_point][current_point]['route']:
                route.append(cell)
    
    tmp = bonus_points[solution[len(solution) - 1]]
    last_point = (tmp[0], tmp[1])
    for cell in distance_saved[last_point][end]['route']:
                route.append(cell)

    return route, visited, cost

def trace(idx, bitmask, isFinish, start, end, distance_saved, bonus_points):
    pre_pos = (-1, -1)
    if idx == len(bonus_points):
        pre_pos = start
    else:
        tmp = bonus_points[idx]
        pre_pos = (tmp[0], tmp[1])
    
    if isFinish == True:
         return
    if (1 << len(bonus_points)) - 1 == bitmask:
        trace(idx, bitmask, True, start, end, distance_saved, bonus_points)
        return
    if dp[idx][bitmask][isFinish] == dp[idx][bitmask][True] + distance_saved[pre_pos][end]['cost']:
        return
    
    for i in range(len(bonus_points)):
        if (bitmask & (1 << i)) != 0: # Đã đi qua điểm thưởng thứ i trước đó rồi
            continue
        point = bonus_points[i]
        if dp[idx][bitmask][isFinish] == dp[i][(bitmask | (1 << i))][isFinish] + distance_saved[pre_pos][(point[0], point[1])]['cost'] + point[2]:
            path.append(i)
            trace(i, (bitmask | (1 << i)), isFinish, start, end, distance_saved, bonus_points)
          

def findMinCost(idx, bitmask, isFinish, start, end, distance_saved, bonus_points): # Quy hoạch động trạng thái bằng đệ quy có nhớ
    pre_pos = (-1, -1)
    if idx == len(bonus_points):
         pre_pos = start
    else:
         tmp = bonus_points[idx]
         pre_pos = (tmp[0], tmp[1])

    if isFinish == True:
         return 0
    if (1 << len(bonus_points)) - 1 == bitmask: # Đã đi qua toàn bộ điểm thưởng
        dp[idx][bitmask][isFinish] = findMinCost(idx, bitmask, True, start, end, distance_saved, bonus_points) + distance_saved[pre_pos][end]['cost']
        return dp[idx][bitmask][isFinish]
    if dp[idx][bitmask][isFinish] != INF: # Trường hợp cấu hình này đã được tính toán trước đó
        return dp[idx][bitmask][isFinish]
    
    cost = INF
    cost = min(cost, findMinCost(idx, bitmask, True, start, end, distance_saved, bonus_points) + distance_saved[pre_pos][end]['cost']) # Quyết định đi thẳng đến EXIT
    
    for i in range(len(bonus_points)):
        if (bitmask & (1 << i)) != 0: # Đã đi qua điểm thưởng thứ i trước đó rồi
            continue
        point = bonus_points[i]
        cost = min(cost, findMinCost(i, (bitmask | (1 << i)), isFinish, start, end, distance_saved, bonus_points) + distance_saved[pre_pos][(point[0], point[1])]['cost'] + point[2]) # Chọn đi tới điểm thưởng thứ i
    
    dp[idx][bitmask][isFinish] = cost
    return dp[idx][bitmask][isFinish]


def DP(matrix, start, end, bonus_points):
    # Tạo mảng dp với kích thước 10 * mask_size * 2 và giá trị ban đầu là 10^10
    global dp
    global path
    path = []
    dp = [[[INF for i in range(2)] for j in range(mask_size)] for k in range(11)]

    distance_saved = setupCostVisitBonusPoint(bonus_points, start, end, matrix)
    cost = findMinCost(len(bonus_points), 0, False, start, end, distance_saved, bonus_points)
    trace(len(bonus_points), 0, False, start, end, distance_saved, bonus_points)

    return getResult(path, bonus_points, distance_saved, start, end, cost)
    
