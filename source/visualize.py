import pygame
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

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 172, 28)
DARK_ORANGE = (139, 64, 0)
GRAY = (128, 128, 128)

GOODBLUE='#20B2AA'

MAZE = []
BONUS=[]
explored=[]
route=[]
start=(0,0)
end=(0,0)
ALGNAME=''
CHEEMSG=None
BANANAS=None
#Init pygame

TILE = 100 #size of each tile
FPS = 60

CELL_WIDTH = 30
CELL_HEIGHT = 30
X_OFFSET = 10
Y_OFFSET = 10
delay = 100
WALL_IMG = pygame.image.load('./assets/fence.png')
START_IMG = pygame.image.load('./assets/star.png')
EXIT_IMG = pygame.image.load('./assets/house.png')
GIFT_IMG = pygame.image.load('./assets/tree.png')
TIM1_IMG = pygame.image.load('./assets/paw.png')
TIM2_IMG = pygame.image.load('./assets/cat.png')

def draw_cell_no_delay(x, y, IMG, WIN):
    drawX = X_OFFSET + y * TILE
    drawY = Y_OFFSET + x * TILE
    WIN.blit(IMG, (drawX, drawY))

def MazeInitialize(MAZE):
    cnt =0;
    bana=[]
    bns=[]
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'x':
                draw_cell_no_delay(row, col, WALL_IMG, screen)

            if MAZE[row][col] == 'v':
                draw_cell_no_delay(row, col, TIM1_IMG, screen)
            # if MAZE[row][col] == ' ':
                # pygame.draw.rect(screen, WHITE, (col * TILE, row * TILE, TILE, TILE))
            if (row,col) == start:
                draw_cell_no_delay(row, col, START_IMG, screen)
            if (row, col) == end:
                draw_cell_no_delay(row, col, EXIT_IMG, screen)
            if MAZE[row][col] == '+':
                bns.append((row,col))
                
            if MAZE[row][col] == 'b':
                bana.append((row,col))
                pygame.draw.rect(screen, GOODBLUE, (col * TILE, row * TILE, TILE, TILE))
    for cell in bns:
        screen.blit(CHEEMSG,(cell[1] * TILE, cell[0] * TILE))          
    for cell in bana:
        screen.blit(BANANAS,(cell[1] * TILE, cell[0] * TILE))
               

def draw_window():
    MazeInitialize(MAZE)


def run_exploredualization(pathIn,alg):
    
    global MAZE ,BONUS,explored,route,start,end,ALGNAME,screen,TILE,CHEEMSG,BANANAS
    BONUS,MAZE=IO.read_file(pathIn)
    if len(MAZE) >= 20 or len(MAZE[0]) >= 20:
        TILE = 30
    else: 
        TILE = 50
    WIDTH = TILE*len(MAZE[0])  # screen width
    HEIGHT = TILE*len(MAZE)  # screen height
    SCREEN_SIZE = [WIDTH, HEIGHT]
    B= list(BONUS.keys())
    start, end = imp.getStartEndPoint(MAZE)
    out = alg(MAZE,start,end,BONUS)
    # explored=list(out[2].keys())
    explored=out[1]
    route=out[0]
    if len(route)>0:
        route.pop(0)
    else:
        print("No route found!")
    TILE=int(HEIGHT/len(MAZE))
    ALGNAME=alg.__name__.upper()
    pygame.init()
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h - 50
    WIDTH = screen_width #screen width
    HEIGHT = screen_height #screen height
    SCREEN_SIZE = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(SCREEN_SIZE) #set screen size
    pygame.display.set_caption("exploredUALIZATION {}".format(ALGNAME)) #set caption

    CHEEMSG=pygame.image.load("./img/gcheems.png").convert_alpha()
    CHEEMSG = pygame.transform.scale(CHEEMSG, (TILE*1.2, TILE*1.2))
    
    BANANAS=pygame.image.load("./img/banana.png").convert_alpha()
    BANANAS=pygame.transform.scale(BANANAS, (TILE, TILE))

    screen.fill((255,255,255))
    algorithm_running = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_window()
        if algorithm_running:
            if len(explored)>0:
               
                current =explored.pop(0)
               
                x=current[0]
                y=current[1]
                if (x,y)==end:
                    explored.clear()
                #mark cell exploredited
                tmp = list(MAZE[x])
                tmp[y]='v'
                # print(current)
                if current in B :
                    tmp[y]='b' #exploredited bonus
                    # screen.blit(CHEEMSG,(y * TILE,x * TILE))
                MAZE[x] = ''.join(tmp)
                # pygame.draw.rect(screen, BLUE, (y * TILE, x * TILE, TILE, TILE))
                pygame.time.wait(2)
                pygame.display.update()
            else:              
                for node in route:
                    # draw_cell_no_delay(node[1]* TILE, node[0]* TILE, GIFT_IMG, screen)
                    # pygame.draw.rect(screen,GREEN, (node[1] * TILE, node[0] * TILE, TILE, TILE))
                    # pygame.draw.circle(screen, GREEN, (node[1] * TILE, node[0] * TILE, TILE, TILE))
                    # add png in route
                    # at the end, dont draw the last node
                    if node == route[-1]:
                        draw_cell_no_delay(node[0], node[1], EXIT_IMG, screen)
                    else:
                        draw_cell_no_delay(node[0], node[1], TIM2_IMG, screen)
                    if node in B:
                        screen.blit(BANANAS,(node[1] * TILE,node[0] * TILE))
                    
                        
                    pygame.time.wait(70)
                    pygame.display.update()
           
                pathIn=Path(pathIn).stem       
                if not os.path.exists('./exploredualize_img'):
                    os.makedirs('./exploredualize_img')
                pygame.image.save(screen, "./exploredualize_img/{}_{}.jpeg".format(ALGNAME,pathIn))
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
    
    path = "../input/level_{0}/input{1}.txt".format(sys.argv[1],sys.argv[2])
    algName=sys.argv[3]
    print("exploredualizing {} on input {}".format(algName,path))
    run_exploredualization(path,alg[algName])
   
   