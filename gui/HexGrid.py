from const import constants as c

import math
import tkinter as tk
from const import constants
from gui.HexCell import Cell

class HexagonalGrid:
    def __init__(self, canvas, size, hex_size, game):
        self.game = game
        self.canvas = canvas
        self.size = size
        self.hex_size = hex_size
        self.cells = []
        self.create_hexagons()

    def create_hexagons(self):
        hex_id = 1
        for col in range(self.size):
            for row in range(self.size):
                x_offset = row * 3/2 * self.hex_size + 1.5 * self.hex_size * (self.size - col)
                y_offset = math.sqrt(3) * self.hex_size * (col + row / 2) - (math.sqrt(3) * self.hex_size / 2) * col
                cell = Cell(self.canvas, x_offset, y_offset + constants.MARGIN_Y, self.hex_size, hex_id, self.game)
                self.cells.append(cell)
                hex_id += 1
        for organism in self.game.get_organisms():
            x = organism.Get_X()
            y = organism.Get_Y() * c.GRID_SIZE
            self.cells[y + x].add_label(organism.GetSymbol())


    def get_clicked(self, x, y):
        clicked_items = self.canvas.find_withtag(tk.CURRENT)
        if clicked_items:
            return self.canvas.gettags(clicked_items[0])[0]