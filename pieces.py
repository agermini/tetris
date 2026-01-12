
"""
Docstring for pieces

O = [[[], []],
     [[], []]]
"""

import pygame
from matrix import ROWS, COLS
import random
import sys

list_of_pieces = []
score = 0

class piece:
    def __init__(self, x: int, y: int):
        """color is represented as a single uppercase character. ex: blue is "B" """
        self.x = x
        self.y = y

    def fallingPiece(self, grid):
        if self.y == ROWS - 1 or self.collision_check_under(grid): 
            self.lock_in(grid)
            Piece_factory.can_hold = True
            lines_cleared = clear_line(grid)
            list_of_pieces.append(Piece_factory.create())
            return lines_cleared
        if self.y < ROWS - 1:
            self.clear_piece(grid)
            self.y += 1
            self.draw_piece(grid)
        return 0

    def lock_in(self, grid):
        for cx, cy in self.get_cells():
            if 0 <= cy < ROWS and 0 <= cx < COLS:
                grid[cy][cx] = [self.color]
        top_row = grid[0]
        for cell in top_row:
            if cell != []:
                pygame.quit()
                sys.exit()
            
    def get_cells(self):
        return [(self.x + dx, self.y + dy) for dx, dy in self.blocks]

    def _set_cells(self, grid, value):
        for x, y in self.get_cells():
            if y < 0:
                continue
            grid[y][x] = value

    def draw_piece(self, grid):
        self._set_cells(grid, [self.color])

    def clear_piece(self, grid):
        self._set_cells(grid, [])
    
    def rotate(self, grid):
        self.clear_piece(grid)
        original_blocks = self.blocks
        self.blocks = [(-y, x) for x, y in self.blocks]
        
        # Check if rotated blocks are out of bounds
        for cell in self.get_cells():
            if cell[1] >= ROWS:
                self.blocks = original_blocks
                return
            if cell[0] < 0:
                self.x += 1
                for cell in self.get_cells():
                    if cell[0] < 0:
                        self.blocks = original_blocks
                        return
            if cell[0] >= COLS:
                self.x -= 1
                for cell in self.get_cells():
                    if cell[0] >= COLS:
                        self.blocks = original_blocks
                        return


        # Check for collisions with locked pieces
        for x, y in self.get_cells():
            if y >= 0 and grid[y][x] != []:
                self.blocks = original_blocks  # Revert rotation
                return

    def collision_check_under(self, grid):
        for cell in self.get_cells():
            test_cell = (cell[0], cell[1] + 1)
            if test_cell in self.get_cells():
                continue
            if test_cell[0] < 0:
                return True
            if test_cell[1] < 0:
                continue
            if test_cell[1] + 1 > ROWS:
                return True
            if grid[test_cell[1]][test_cell[0]] != []:
                return True
        return False
    
    def move_left(self, grid: list[list]):
        self.clear_piece(grid)
        if not self.collision_check_left(grid):
            self.x -= 1

    def collision_check_left(self, grid: list[list]):
        cells = self.get_cells()
        for cell in cells:
            test_cell = (cell[0] - 1, cell[1])
            if test_cell in cells:
                continue
            if test_cell[0] < 0:
                return True
            if test_cell[1] < 0:
                continue
            elif grid[test_cell[1]][test_cell[0]] != []:
                    return True
        return False

    def move_right(self, grid: list[list]):
        self.clear_piece(grid)
        if not self.collision_check_right(grid):
            self.x += 1

    def collision_check_right(self, grid: list[list]):
        cells = self.get_cells()
        for cell in cells:
            test_cell = (cell[0] + 1, cell[1])
            if test_cell in cells:
                continue
            if test_cell[0] >= COLS:
                return True
            if test_cell[1] < 0:
                continue
            elif grid[test_cell[1]][test_cell[0]] != []:
                return True
        return False
    
def clear_line(grid: list[list]):
    bool = False
    for i in range(len(grid)):
        if [] not in grid[i]:
            grid.pop(i)
            grid.insert(0, [[] for _ in range(COLS)])
            bool = True
            global score
            score += 10
            update_highscore()
    return bool

def update_highscore():
    with open ("./highscore.txt", "r") as file:
        lines = file.readlines()
        highscore = int(lines[0])
    with open ("./highscore.txt", "w") as file:
        if score > highscore:
            file.write(str(score))
            
class O_block(piece):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "Y"
        self.blocks = [(0,0), (1,0), (0,-1), (1,-1)]

    def rotate(self, grid):
        pass
    
class I_block(piece):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "C"
        self.blocks = [(0,0), (-1,0), (1,0), (2,0)]

class L_block(piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "O"
        self.blocks = [(0,0), (1,0), (0,-1), (0,-2)]

class J_block(piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "Pi"
        self.blocks = [(0,0), (-1,0), (0,-1), (0,-2)]
    
class T_block(piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "Pu"
        self.blocks = [(0,0), (-1,0), (1,0), (0,-1)]

class S_block(piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "R"
        self.blocks = [(0,0), (-1,0),(0,-1),(1,-1)]

class Z_block(piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "G"
        self.blocks = [(0,0), (1,0),(0,-1),(-1,-1)]

class Piece_factory:

    PIECES = [O_block, I_block, L_block, J_block, T_block, S_block, Z_block]

    COLORS = ['R', 'B', 'P', 'Y', 'G', 'C']

    can_hold = True

    @staticmethod
    def create():
        """create randomized piece"""
        PieceClass = random.choice(Piece_factory.PIECES)
        return PieceClass(4, 0)
    @staticmethod
    def create_copy(piece: piece):
        """Create a copy of a piece"""
        return piece.__class__(4, 0)
        