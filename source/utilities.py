import pygame
import imageio
import numpy as np
from pygame.locals import QUIT
import sys, os
import implement as imp
from pathlib import Path
from implement import *
from BFS import *
from DFS import *
from UCS import *
from GBFS import *
from A_Star import *
from BFS_Tele import *
from HILL_CLIMBING import *
from GENETIC import *
from A_Star_lv2 import *
from DP import *
from DIJKSTRA import *



matrix = []
BONUS = []
explored = []
frames = []
route = []
start = (0,0)
end = (0,0)
ALGNAME = ''
scale = 100
FPS = 30
CELL_WIDTH = 30
CELL_HEIGHT = 30
X_OFFSET = 10
Y_OFFSET = 10
delay = 1000

WALL_IMG = pygame.image.load('./source/assets/fence.png')
START_IMG = pygame.image.load('./source/assets/star.png')
FAIL_IMG = pygame.image.load('./source/assets/fail.png')
EXIT_IMG = pygame.image.load('./source/assets/house.png')
GIFT_IMG = pygame.image.load('./source/assets/tree.png')
TIM1_IMG = pygame.image.load('./source/assets/paw.png')
TIM2_IMG = pygame.image.load('./source/assets/cat.png')
CLOSE_IMG = pygame.image.load('./source/assets/close.png')
OPEN_IMG = pygame.image.load('./source/assets/open.png')
TELEPORT = pygame.image.load('./source/assets/tele.png')
TELEPORT_OUT = pygame.image.load('./source/assets/teleout.png')

TIM_U_IMG = pygame.image.load('./source/assets/cat.png')
TIM_L_IMG = pygame.image.load('./source/assets/cat_l.png')
TIM_R_IMG = pygame.image.load('./source/assets/cat_r.png')
TIM_D_IMG = pygame.image.load('./source/assets/cat_d.png')

RETIM_U_IMG = pygame.image.load('./source/assets/recat_u.png')
RETIM_L_IMG = pygame.image.load('./source/assets/recat_l.png')
RETIM_R_IMG = pygame.image.load('./source/assets/recat_r.png')
RETIM_D_IMG = pygame.image.load('./source/assets/recat_d.png')

alg = {}
alg["dfs"] = DFS
alg["bfs"] = BFS
alg["ucs"] = UCS
alg["gbfs_heuristic_1"] = GBFS_heuristic_1
alg["gbfs_heuristic_2"] = GBFS_heuristic_2
alg["dijkstra"] = Dijkstra
alg["astar_heuristic_1"] = AStar_heuristic_1
alg["astar_heuristic_2"] = AStar_heuristic_2
alg["astar_lv2_heuristic_1"] = AStar_Lv2_heuristic_1
alg["astar_lv2_heuristic_2"] = AStar_Lv2_heuristic_2
alg["hill_climbing"] = HILL_CLIMBING
alg["genetic"] = GENETIC
alg["bfs_tele"] = BFS_Tele
alg["dp"] = DP    

def scale_image(scale):
    global WALL_IMG, START_IMG, EXIT_IMG, GIFT_IMG, TIM1_IMG, TIM2_IMG, CLOSE_IMG, OPEN_IMG, TELEPORT, TELEPORT_OUT
    global TIM_R_IMG, TIM_L_IMG, TIM_U_IMG, TIM_D_IMG, RETIM_D_IMG, RETIM_U_IMG, RETIM_L_IMG, RETIM_R_IMG, FAIL_IMG

    WALL_IMG = pygame.transform.scale(WALL_IMG, (scale, scale))
    START_IMG = pygame.transform.scale(START_IMG, (scale, scale))
    EXIT_IMG = pygame.transform.scale(EXIT_IMG, (scale, scale))
    GIFT_IMG = pygame.transform.scale(GIFT_IMG, (scale, scale))
    TIM1_IMG = pygame.transform.scale(TIM1_IMG, (scale, scale))
    TIM2_IMG = pygame.transform.scale(TIM2_IMG, (scale, scale))
    CLOSE_IMG = pygame.transform.scale(CLOSE_IMG, (scale, scale))
    OPEN_IMG = pygame.transform.scale(OPEN_IMG, (scale, scale))
    TELEPORT = pygame.transform.scale(TELEPORT, (scale, scale))
    TELEPORT_OUT = pygame.transform.scale(TELEPORT_OUT, (scale, scale))
    TIM_U_IMG = pygame.transform.scale(TIM_U_IMG, (scale, scale))
    TIM_L_IMG = pygame.transform.scale(TIM_L_IMG, (scale, scale))
    TIM_R_IMG = pygame.transform.scale(TIM_R_IMG, (scale, scale))
    TIM_D_IMG = pygame.transform.scale(TIM_D_IMG, (scale, scale))
    RETIM_U_IMG = pygame.transform.scale(RETIM_U_IMG, (scale, scale))
    RETIM_L_IMG = pygame.transform.scale(RETIM_L_IMG, (scale, scale))
    RETIM_R_IMG = pygame.transform.scale(RETIM_R_IMG, (scale, scale))
    RETIM_D_IMG = pygame.transform.scale(RETIM_D_IMG, (scale, scale))
    FAIL_IMG = pygame.transform.scale(FAIL_IMG, (scale, scale))

def draw_cell_no_delay(x, y, IMG, WIN):
    drawX = X_OFFSET + y * CELL_WIDTH
    drawY = Y_OFFSET + x * CELL_HEIGHT
    WIN.blit(IMG, (drawX, drawY))

def matrix_initialize(matrix, scale):
    plus = []
    bns = []

    scale_image(scale)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'x':
                draw_cell_no_delay(row, col, WALL_IMG, screen)

            if matrix[row][col] == 'v':
                draw_cell_no_delay(row, col, TIM1_IMG, screen)
            # if matrix[row][col] == ' ':
                # pygame.draw.rect(screen, WHITE, (col * scale, row * scale, scale, scale))
            if (row,col) == start:
                draw_cell_no_delay(row, col, START_IMG, screen)
            if (row, col) == end:
                draw_cell_no_delay(row, col, EXIT_IMG, screen)
            if  matrix[row][col] == 'o':
                draw_cell_no_delay(row, col, TELEPORT, screen)
            if matrix[row][col] == 'O':
                draw_cell_no_delay(row, col, TELEPORT_OUT, screen)
            if matrix[row][col] == '+':
                bns.append((row,col))
                
            if matrix[row][col] == 'b':
                plus.append((row,col))
                # pygame.draw.rect(screen, GOODBLUE, (col * scale, row * scale, scale, scale))
            # if matrix[row][col] == 'O' or matrix[row][col] == 'o':
            #     plus.append((row,col))
            #     pygame.draw.rect(screen, GOODBLUE, (col * scale, row * scale, scale, scale))
    for cell in bns:
        draw_cell_no_delay(cell[0], cell[1], OPEN_IMG, screen)      
    # for cell in plus:
    #     draw_cell_no_delay(cell[0], cell[1], CLOSE_IMG, screen)

def draw_map():
    matrix_initialize(matrix, scale)


def path_finding(dir, alg, algName, level, input):
    global matrix ,BONUS, explored, route, start, end, ALGNAME, screen, scale
    BONUS, matrix, is_teleport = read_file(dir)
    print("matrix size: ", len(matrix), len(matrix[0]))

    B = [(point[0], point[1]) for point in BONUS]
    B_OUT = []
    if is_teleport:
        B_OUT = [(point[2], point[3]) for point in BONUS]
    start, end = imp.getStartEndPoint(matrix)

    out = alg(matrix,start,end,BONUS)
    route = out[0]
    explored = out[1]
    cost = out[2]
    if len(route) > 0:
        route.pop(0)
    else:
        print("No route found!")

    ALGNAME=alg.__name__.lower()
    write_cost_path(cost, './output/' + level + '/' + input + '/' + algName  + '/' + ALGNAME + '.txt')

    pygame.init()
    display_info = pygame.display.Info()
    SCREEN_WIDTH = display_info.current_w
    SCREEN_HEIGHT = display_info.current_h - 50
    SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]

    global CELL_WIDTH, CELL_HEIGHT
    if SCREEN_WIDTH / len(matrix[0]) < SCREEN_HEIGHT / len(matrix):
        CELL_WIDTH = CELL_HEIGHT = (SCREEN_WIDTH) / (len(matrix[0]) + 2) 
    else:
        CELL_WIDTH = CELL_HEIGHT = (SCREEN_HEIGHT) / (len(matrix) + 2)
    scale = CELL_WIDTH
    scale_image(scale)

    global X_OFFSET, Y_OFFSET
    X_OFFSET = (SCREEN_WIDTH - len(matrix[0]) * CELL_WIDTH) // 2
    Y_OFFSET = (SCREEN_HEIGHT - len(matrix) * CELL_HEIGHT) // 2

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Video mô tả {}".format(ALGNAME)) #set caption

    screen.fill((255,255,255))
    # output_file = "output_video.mp4"
    # writer = imageio.get_writer(output_file, fps=FPS, macro_block_size=None)
    # for frame in frames:
    #     writer.append_data(frame)
    output_file = "./output/" + level + "/" + input + "/" + algName + '/' + ALGNAME + ".mp4" 
    FPS = 30  # Frames per second (adjust as needed)
    writer = imageio.get_writer(output_file, fps=FPS, macro_block_size=None)
    algorithm_running = True
    clock = pygame.time.Clock()
    while True:
        frame = pygame.surfarray.array3d(screen)
        frame = np.flip(frame, axis=1)
        frame = np.rot90(frame)
        writer.append_data(frame)

        pygame.display.update()
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_map()
        # print(len(explored))
        if algorithm_running:
            if len(explored) > 0:
                current = explored.pop(0)
                x = current[0]
                y = current[1]
                # if (x,y)==end:
                #     explored.clear()
                tmp = list(matrix[x])
                tmp[y] = 'v'
                if current in B :
                    tmp[y] = 'b' #exploredited bonus
                matrix[x] = ''.join(tmp)
                pygame.time.wait(2)
                pygame.display.update()
            else:    
                route_footed = []          
                for i in range(len(route)):
                    node = route[i]
                    
                    if node == route[-1]:
                        if node == end:
                            draw_cell_no_delay(node[0], node[1], EXIT_IMG, screen)
                        else: 
                            draw_cell_no_delay(node[0], node[1], FAIL_IMG, screen)
                        continue
                    next_node = route[i+1]
                    if next_node[0]-node[0]>0:
                        DRAW_ASSET = TIM_D_IMG if node not in route_footed else RETIM_D_IMG
                        # direction.append('v') #^
                    elif next_node[0]-node[0] < 0:
                        DRAW_ASSET = TIM_U_IMG if node not in route_footed else RETIM_U_IMG
                        # direction.append('^') #v        
                    elif next_node[1]-node[1] > 0:
                        DRAW_ASSET = TIM_R_IMG if node not in route_footed else RETIM_R_IMG
                        # direction.append('>')
                    else:
                        DRAW_ASSET = TIM_L_IMG if node not in route_footed else RETIM_L_IMG
                        # direction.append('<')
                    draw_cell_no_delay(node[0], node[1], DRAW_ASSET, screen)
                    
                    if not is_teleport:
                        if node in B:
                            draw_cell_no_delay(node[0], node[1], CLOSE_IMG, screen)
                    else:
                        if node in B:
                            draw_cell_no_delay(node[0], node[1], TELEPORT, screen)
                        if node in B_OUT:
                            draw_cell_no_delay(node[0], node[1], TELEPORT_OUT, screen)
                    route_footed.append(node)

                    frame = pygame.surfarray.array3d(screen)
                    frame = np.flip(frame, axis=1)
                    frame = np.rot90(frame)
                    writer.append_data(frame)    
                    pygame.time.wait(70)
                    pygame.display.update()
                    clock.tick(FPS)
           
                dir=Path(dir).stem       
                # if not os.path.exists('./exploredualize_img'):
                #     os.makedirs('./exploredualize_img')
                pygame.image.save(screen, "./output/{}/{}/{}/{}.jpg".format(level, input,algName, ALGNAME))
                algorithm_running = False
            pygame.time.wait(50)
            
        else:
            pygame.time.wait(3000)
            writer.close()
            pygame.quit()
            sys.exit() 

