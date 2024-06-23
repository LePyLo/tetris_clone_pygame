from grid import Grid
from enum import Enum
from random import choice
from blocks import *

class GameState(Enum):
    RUNNING = 0
    ENDED = 1

class Game:
    def __init__(self):
        self.game_state = GameState.RUNNING
        self.time_accum = 0
        self.time_limit = 0.5  #segundos
        self.grid = Grid()
        self.game_over = False
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = choice(self.blocks)
        self.blocks.remove(block)
        return block
    def move_left(self):
        self.current_block.move(0,-1)
        if not self.block_inside() or not self.block_fits() :
            self.current_block.move(0,1)
    def move_right(self):
        self.current_block.move(0,1)
        if not self.block_inside() or not self.block_fits() :
            self.current_block.move(0,-1)
    def move_down(self):
        self.current_block.move(1,0)
        if not self.block_inside() or not self.block_fits() :
            self.current_block.move(-1,0)
            self.lock_block()
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_rows()
        if not self.block_fits():
            self.game_over = True
    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()
        
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            if not self.grid.is_inside(position.row, position.column):
                return False
        return True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            if not self.grid.is_empty(position.row, position.column):
                return False
        return True

    def update(self,dt):
        print(self.game_over)
        if self.time_accum < self.time_limit:
            self.time_accum+=dt
        else:
            self.move_down()
            self.time_accum=0
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)