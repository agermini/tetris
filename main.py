import pygame
pygame.init()


import matrix
import pieces
from pieces import Piece_factory
from pieces import list_of_pieces

list_of_pieces.append(Piece_factory.create(4, 0))

initial_width = 900
initial_height = 900
screen = pygame.display.set_mode((initial_width, initial_height))
grid_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

clock = pygame.time.Clock()
running = True

slow_fall_delay = 500
fast_fall_delay = 100
fall_delay = slow_fall_delay
fall_timer = 0

current_piece = list_of_pieces[-1]

while running:

    dt = clock.get_time()
    fall_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_piece.move_left(matrix.tetris_grid)
            if event.key == pygame.K_RIGHT:
                current_piece.move_right(matrix.tetris_grid)
            if event.key == pygame.K_DOWN:
                fall_delay = fast_fall_delay
            if event.key == pygame.K_SPACE:
                current_piece.rotate(matrix.tetris_grid)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                fall_delay = slow_fall_delay

    if fall_timer >= fall_delay:
        current_piece.fallingPiece(matrix.tetris_grid)
        fall_timer = 0

    screen.fill('black')
    grid_surface.fill((0,0,0,0))

    # RENDER GAME HERE
    current_piece = list_of_pieces[-1]
    current_piece.draw_piece(matrix.tetris_grid)

    matrix.draw_grid(matrix.tetris_grid, grid_surface)
    screen.blit(grid_surface)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()