from const import constants as c

import math
import tkinter as tk
from const import constants


class Cell:
    def __init__(self, canvas, x, y, size, id, game):
        self.game = game
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.id = id
        self.polygon = self.draw()
        #self.label = self.add_label()
        self.bind_click()

    def draw(self):
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            x = self.x + self.size * math.cos(angle)
            y = self.y + self.size * math.sin(angle)
            points.append((x, y))
        return self.canvas.create_polygon(points, outline='black', fill='white', tags=str(self.id))

    def add_label(self, symbol):
        return self.canvas.create_text(self.x, self.y, text=str(symbol), tags=str(self.id))

    def bind_click(self):
        self.canvas.tag_bind(self.polygon, "<Button-1>", self.on_click)
        #self.canvas.tag_bind(self.label, "<Button-1>", self.on_click)

    def on_click(self, event):
        self.game.add_organims_to_cell(self.canvas, event.x_root, event.y_root, self.id)

