from colors import Color
import pygame as pg

from position import Position
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.row_offset = 0
        self.column_offset = 0
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Color.get_cell_colors()
    
    def move(self, rows, columns):
        self.row_offset+=rows
        self.column_offset+=columns

    def rotate(self):
        self.rotation_state+=1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row+self.row_offset, position.column+self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pg.rect.Rect(
                tile.column*self.cell_size, 
                tile.row*self.cell_size, 
                self.cell_size, 
                self.cell_size)
            pg.draw.rect(screen, self.colors[self.id],tile_rect)

