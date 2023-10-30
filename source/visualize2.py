import pygame

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

WALL_IMG = pygame.image.load('./assets/tree.png')
START_IMG = pygame.image.load('./assets/tree.png')
EXIT_IMG = pygame.image.load('./assets/tree.png')
GIFT_IMG = pygame.image.load('./assets/tree.png')


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


def main():
    pygame.init()

    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h - 50
    WIN = pygame.display.set_mode((screen_width, screen_height))  # Kích thước cửa sổ pygame
    WIN.fill(WHITE)

    # Tính toán kích thước mê cung dựa trên số hàng và số cột
    maze_height = len(maze_matrix) * CELL_HEIGHT
    maze_width = len(maze_matrix[0]) * CELL_WIDTH

    # Tính toán vị trí bắt đầu để vẽ mê cung giữa cửa sổ pygame
    global X_OFFSET, Y_OFFSET
    X_OFFSET = (screen_width - maze_width) // 2
    Y_OFFSET = (screen_height - maze_height) // 2

    draw_maze(maze_matrix, WIN)
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
    main()