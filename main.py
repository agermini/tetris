import pygame
pygame.init()


import matrix
from pieces import Piece_factory
from pieces import list_of_pieces

list_of_pieces.append(Piece_factory.create())

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

stored = None
lines_cleared = 0

pygame.mixer.init()
pygame.mixer.music.load("tetris_theme.wav")
#pygame.mixer.music.play(-1)

while running:

    dt = clock.get_time()
    fall_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                current_piece.move_left(matrix.tetris_grid)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                current_piece.move_right(matrix.tetris_grid)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                fall_delay = fast_fall_delay
            if event.key == pygame.K_SPACE:
                current_piece.rotate(matrix.tetris_grid)
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and Piece_factory.can_hold:
                if stored is None:
                    current_piece.clear_piece(matrix.tetris_grid)
                    stored = current_piece
                    current_piece = Piece_factory.create()
                else:
                    current_piece.clear_piece(matrix.tetris_grid)
                    temp = stored
                    stored = current_piece
                    current_piece = Piece_factory.create_copy(temp)
                list_of_pieces[-1] = current_piece
                Piece_factory.can_hold = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                fall_delay = slow_fall_delay

    speed = fall_delay - lines_cleared*10
    if speed < 0:
        speed = 0

    if fall_timer >= speed:
        lines_cleared += current_piece.fallingPiece(matrix.tetris_grid)
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