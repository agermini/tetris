import pygame

red = ['R']
purple = ['Pu']
pink = ['Pi']
yellow = ['Y']
green = ['G']
cyan = ['C']
orange = ['O']

trans_white = pygame.Color(255, 255, 255, 150)

tetris_grid = \
[[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],]

ROWS = len(tetris_grid)
COLS = len(tetris_grid[0])
cell_size = 35

def draw_grid(grid: list[list], surface: pygame.Surface):

    offset_x = 300
    offset_y = 50

    ### Draw cells
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * cell_size + offset_x,
                row * cell_size + offset_y,
                cell_size,
                cell_size
            )
            square = grid[row][col]
            if square == []:
                continue
            if square == red:
                pygame.draw.rect(surface, 'red', rect, 0)
            if square == pink:
                pygame.draw.rect(surface, 'pink', rect, 0)
            if square == purple:
                pygame.draw.rect(surface, 'purple', rect, 0)
            if square == yellow:
                pygame.draw.rect(surface, 'yellow', rect, 0)
            if square == green:
                pygame.draw.rect(surface, 'green', rect, 0)
            if square == cyan:
                pygame.draw.rect(surface, 'cyan', rect, 0)
            if square == orange:
                pygame.draw.rect(surface, 'orange', rect, 0)

    ### Draw grid lines
    for row in range(ROWS + 1):
        line = pygame.Rect( 
                offset_x,
                row * cell_size + offset_y, 
                COLS * cell_size, 
                1)
        pygame.draw.rect(surface, trans_white, line, 0)
    for col in range(COLS + 1):
        line = pygame.Rect(
                col * cell_size + offset_x,
                offset_y,
                1,
                ROWS * cell_size
        )
        pygame.draw.rect(surface, trans_white, line, 0)


            