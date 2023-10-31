import pygame
import imageio
import numpy as np
from pygame.locals import QUIT
import sys,os
import processIO as IO
import implement as imp
from pathlib import Path
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
from implement import *

matrix = []
BONUS=[]
explored=[]
route=[]
start=(0,0)
end=(0,0)
ALGNAME=''
scale = 100
FPS = 60
CELL_WIDTH = 30
CELL_HEIGHT = 30
SCREEN_WIDTH = 1280  # 16:9 aspect ratio
SCREEN_HEIGHT = 720
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
map_width = scale * len(matrix[0]) if matrix else 0
map_height = scale * len(matrix)
map_x = (SCREEN_WIDTH - map_width) // 2
map_y = (SCREEN_HEIGHT - map_height) // 2
X_OFFSET = 10
Y_OFFSET = 10
delay = 100
WALL_IMG1 = pygame.image.load('./assets/fence.png')
START_IMG1 = pygame.image.load('./assets/star.png')
EXIT_IMG1 = pygame.image.load('./assets/house.png')
GIFT_IMG1 = pygame.image.load('./assets/tree.png')
TIM1_IMG1 = pygame.image.load('./assets/paw.png')
TIM2_IMG1 = pygame.image.load('./assets/cat.png')
CLOSE_IMG1 = pygame.image.load('./assets/close.png')
OPEN_IMG1 = pygame.image.load('./assets/open.png')
TELEPORT1 = pygame.image.load('./assets/tele.png')
TELEPORT_OUT1 = pygame.image.load('./assets/teleout.png')

def draw_cell_no_delay(x, y, IMG, WIN):
    drawX = map_x + y * scale
    drawY = map_y + x * scale
    WIN.blit(IMG, (drawX, drawY))

def matrix_initialize(matrix,scale):
    cnt =0
    plus=[]
    bns=[]
    WALL_IMG = pygame.transform.scale(WALL_IMG1, (scale, scale))
    START_IMG = pygame.transform.scale(START_IMG1, (scale, scale))
    EXIT_IMG = pygame.transform.scale(EXIT_IMG1, (scale, scale))
    GIFT_IMG = pygame.transform.scale(GIFT_IMG1, (scale, scale))
    TIM1_IMG = pygame.transform.scale(TIM1_IMG1, (scale, scale))
    TIM2_IMG = pygame.transform.scale(TIM2_IMG1, (scale, scale))
    CLOSE_IMG = pygame.transform.scale(CLOSE_IMG1, (scale, scale))
    OPEN_IMG = pygame.transform.scale(OPEN_IMG1, (scale, scale))
    TELEPORT = pygame.transform.scale(TELEPORT1, (scale, scale))
    TELEPORT_OUT = pygame.transform.scale(TELEPORT_OUT1, (scale, scale))
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
    for cell in plus:
        draw_cell_no_delay(cell[0], cell[1], CLOSE_IMG, screen)

def draw_map():
    matrix_initialize(matrix,scale)


def path_finding(dir,alg):
    global matrix ,BONUS,explored,route,start,end,ALGNAME,screen,scale
    BONUS,matrix, is_teleport= read_file(dir)
    print("matrix size: ",len(matrix),len(matrix[0]))
    if len(matrix) >= 15 or len(matrix[0]) >= 35:
        scale = 20
        
    else: 
        scale = 30
    WALL_IMG = pygame.transform.scale(WALL_IMG1, (scale, scale))
    START_IMG = pygame.transform.scale(START_IMG1, (scale, scale))
    EXIT_IMG = pygame.transform.scale(EXIT_IMG1, (scale, scale))
    GIFT_IMG = pygame.transform.scale(GIFT_IMG1, (scale, scale))
    TIM1_IMG = pygame.transform.scale(TIM1_IMG1, (scale, scale))
    TIM2_IMG = pygame.transform.scale(TIM2_IMG1, (scale, scale))
    CLOSE_IMG = pygame.transform.scale(CLOSE_IMG1, (scale, scale))
    OPEN_IMG = pygame.transform.scale(OPEN_IMG1, (scale, scale))
    TELEPORT = pygame.transform.scale(TELEPORT1, (scale, scale))
    TELEPORT_OUT = pygame.transform.scale(TELEPORT_OUT1, (scale, scale))
    WIDTH = scale*len(matrix[0])  # screen width
    HEIGHT = scale*len(matrix)  # screen height
    SCREEN_SIZE = [WIDTH, HEIGHT]
    # B= list(BONUS.keys())
    B = [(point[0], point[1]) for point in BONUS]
    B_OUT = []
    if is_teleport:
        B_OUT = [(point[2], point[3]) for point in BONUS]
    start, end = imp.getStartEndPoint(matrix)

    out = alg(matrix,start,end,BONUS)
    explored=out[1]
    route=out[0]
    if len(route)>0:
        route.pop(0)
    else:
        print("No route found!")
    scale=int(HEIGHT/len(matrix))
    ALGNAME=alg.__name__.upper()
    pygame.init()
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h - 50
    SCREEN_WIDTH = 1280  # 16:9 aspect ratio
    SCREEN_HEIGHT = 720
    SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen = pygame.display.set_mode(SCREEN_SIZE) #set screen size
    pygame.display.set_caption("exploredUALIZATION {}".format(ALGNAME)) #set caption

    screen.fill((255,255,255))
    output_file = "output_video.mp4"
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
        if algorithm_running:
            if len(explored)>0:
                current =explored.pop(0)
                x=current[0]
                y=current[1]
                if (x,y)==end:
                    explored.clear()
                tmp = list(matrix[x])
                tmp[y]='v'
                if current in B :
                    tmp[y]='b' #exploredited bonus
                matrix[x] = ''.join(tmp)
                pygame.time.wait(2)
                pygame.display.update()
            else:              
                for node in route:
                    
                    if node == route[-1]:
                        draw_cell_no_delay(node[0], node[1], EXIT_IMG, screen)
                    else:
                        draw_cell_no_delay(node[0], node[1], TIM2_IMG, screen)
                    if not is_teleport:
                        if node in B:
                            draw_cell_no_delay(node[0], node[1], CLOSE_IMG, screen)
                    else:
                        if node in B:
                            draw_cell_no_delay(node[0], node[1], TELEPORT, screen)
                        if node in B_OUT:
                            draw_cell_no_delay(node[0], node[1], TELEPORT_OUT, screen)



                    
          
                    pygame.time.wait(70)
                    pygame.display.update()
           
                dir=Path(dir).stem       
                if not os.path.exists('./exploredualize_img'):
                    os.makedirs('./exploredualize_img')
                pygame.image.save(screen, "./exploredualize_img/{}_{}.jpeg".format(ALGNAME,dir))
                algorithm_running = False
            pygame.time.wait(50)
            
        else:
            pygame.time.wait(3000)
            
            pygame.quit()
            sys.exit()

alg={}
alg["dfs"]=DFS_main
alg["bfs"]=BFS
alg["ucs"]=UCS
alg["gbfs1"]=GBFS
alg["Dijkstra"]=Dijkstra
alg["astar1"]=AStar
alg["astar2"]=AStar_Lv2
alg["adv"]=HILL_CLIMBING
alg["genetic"]=GENETIC
alg["bfs_tele"]=BFS_Tele
alg["dp"]=DP     


if __name__ == "__main__":
    if 'advance' == sys.argv[1]:
        path = "../input/advance/input{0}.txt".format(sys.argv[2])
    else:    
        path = "../input/level_{0}/input{1}.txt".format(sys.argv[1],sys.argv[2])
    algName=sys.argv[3]
    print("exploredualizing {} on input {}".format(algName,path))
    path_finding(path,alg[algName])
   
   