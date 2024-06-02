import tkinter as tk
import math
from tkinter import messagebox

from const import constants as c
from const import constants
from game.World import World

class SquareGrid:
    def __init__(self, canvas, size, square_size, game):
        self.game = game
        self.canvas = canvas
        self.size = size
        self.square_size = square_size
        self.create_squares()


    def create_squares(self):
        square_id = 1
        for row in range(self.size):
            for col in range(self.size):
                x = col * self.square_size + constants.MARGIN_X
                y = row * self.square_size + constants.MARGIN_Y
                rect = self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size, outline='black', fill='white', tags=str(square_id))
                #label = self.canvas.create_text(x + self.square_size / 2, y + self.square_size / 2, text=str(square_id), tags=str(square_id))
                #self.canvas.tag_bind(rect, "<Button-1>", lambda event, rect=rect: self.on_click(rect))
                #self.canvas.tag_bind(label, "<Button-1>", lambda event, rect=rect: self.on_click(rect))
                square_id += 1
        for organism in self.game.get_organisms():
            x = organism.get_x() * self.square_size + constants.MARGIN_X
            y = organism.get_y() * self.square_size + constants.MARGIN_Y
            label = self.canvas.create_text(x + self.square_size / 2, y + self.square_size / 2, text=str(organism.get_symbol()),tags=str(square_id))

    def on_click(self, event, rect):
        self.canvas.itemconfig(rect, fill='yellow')
        #print(f"Clicked square with ID: {self.canvas.gettags(rect)[0]}")
        # event.X_root and  y are the loacation where the window should be displayed
        self.game.add_organism_to_cell(self.canvas, event.x_root, event.y_root, rect)

    def get_clicked(self, x, y):
        clicked_items = self.canvas.find_withtag(tk.CURRENT)
        if clicked_items:
            return self.canvas.gettags(clicked_items[0])[0]