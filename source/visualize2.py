import pygame
import sys,os
from implement import read_file

FPS = 60
CELL_WIDTH = 30
CELL_HEIGHT = 30
X_OFFSET = 10
Y_OFFSET = 10
delay = 100


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
GRAY = (128, 128, 128)

maze_matrix = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'S', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' '],
]

# WALL_IMG = pygame.image.load('./assets/tree.png')
# START_IMG = pygame.image.load('./assets/tree.png')
# EXIT_IMG = pygame.image.load('./assets/tree.png')
# GIFT_IMG = pygame.image.load('./assets/tree.png')

WALL_IMG = pygame.image.load('./assets/fence.png')
START_IMG = pygame.image.load('./assets/star.png')
EXIT_IMG = pygame.image.load('./assets/house.png')
GIFT_IMG = pygame.image.load('./assets/tree.png')
TIM1_IMG = pygame.image.load('./assets/paw.png')
TIM_U_IMG = pygame.image.load('./assets/cat.png')
TIM_L_IMG = pygame.image.load('./assets/cat_l.png')
TIM_R_IMG = pygame.image.load('./assets/cat_r.png')
TIM_D_IMG = pygame.image.load('./assets/cat_d.png')

RETIM_U_IMG = pygame.image.load('./assets/recat_u.png')
RETIM_L_IMG = pygame.image.load('./assets/recat_l.png')
RETIM_R_IMG = pygame.image.load('./assets/recat_r.png')
RETIM_D_IMG = pygame.image.load('./assets/recat_d.png')

CLOSE_IMG = pygame.image.load('./assets/close.png')
OPEN_IMG = pygame.image.load('./assets/open.png')
TELEPORT = pygame.image.load('./assets/tele.png')
TELEPORT_OUT = pygame.image.load('./assets/teleout.png')


def draw_maze(matrix, WIN):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            cell = matrix[row][col]
            
            if cell == 'x':
                draw_cell_no_delay(row, col, WALL_IMG, WIN)
            elif cell == 'S':
                draw_cell_no_delay(row, col, START_IMG, WIN)
            elif row == 0 or row == rows - 1 or col == 0 or col == cols - 1:    
                draw_cell_no_delay(row, col, EXIT_IMG, WIN)
            elif cell == '+':
                draw_cell_no_delay(row, col, GIFT_IMG, WIN)


def draw_cell_no_delay(x, y, IMG, WIN):
    drawX = X_OFFSET + y * CELL_WIDTH
    drawY = Y_OFFSET + x * CELL_HEIGHT
    WIN.blit(IMG, (drawX, drawY))

def draw_cell(x, y, IMG, WIN):
    drawX = X_OFFSET + y * CELL_WIDTH
    drawY = Y_OFFSET + y * CELL_HEIGHT
    WIN.blit(IMG, (drawX, drawY))
    pygame.display.update()
    pygame.time.delay(delay)


def main(matrix):
    pygame.init()

    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h - 50
    WIN = pygame.display.set_mode((screen_width, screen_height))  # Kích thước cửa sổ pygame
    WIN.fill(WHITE)

    # Tính toán kích thước mê cung dựa trên số hàng và số cột
    maze_height = len(matrix) * CELL_HEIGHT
    maze_width = len(matrix[0]) * CELL_WIDTH

    # Tính toán vị trí bắt đầu để vẽ mê cung giữa cửa sổ pygame
    global X_OFFSET, Y_OFFSET
    X_OFFSET = (screen_width - maze_width) // 2
    Y_OFFSET = (screen_height - maze_height) // 2

    draw_maze(matrix, WIN)
    pygame.display.update()
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    if 'advance' == sys.argv[1]:
        path = "../input/advance/input{0}.txt".format(sys.argv[2])
    else:    
        path = "../input/level_{0}/input{1}.txt".format(sys.argv[1],sys.argv[2])
    BONUS,matrix, is_teleport= read_file(path)
    main(matrix)