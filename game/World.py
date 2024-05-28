from const import constants as c
import tkinter as tk
from game.Wolf import Wolf


class World:
    def __init__(self, MainWidnow):
        self.__organisms = []
        self.__is_hex = False
        self.__list_of_organisms = {"Wolf", "Sheep", "Fox", "Turtle", "Antelope", "Cyber_sheep", "Grass", "Thistle", "Guarana", "Belladonna", "Sosnowsky_hogweed"}
        self.__size = 0
        self.__size_at_begining = 0
        self.__turn = 0
        self.__MainWindow = MainWidnow
        self.__key = ""
        print("World created")

    def legal_field(self, current_x, current_y, direction_x, direction_y, speed):
        if (current_x + (direction_x * speed)) >= 0 and (current_x + (direction_x * speed)) < c.GRID_SIZE:
            if (current_y + (direction_y * speed)) >= 0 and (current_y + (direction_y * speed)) < c.GRID_SIZE:
                return True
        return False

    def search_for_free_space(self, xy, x, y, sawing):
        xy[0] = -1
        xy[1] = -1

        if self._game.legal_field(x, y, c.LEFT, 0, 1) and not self._game.collide(0, False, x + c.LEFT, y):
            xy[0] = x + c.LEFT
            xy[1] = y
        elif self._game.legal_field(x, y, c.RIGHT, 0, 1) and not self._game.collide(0, False, x + c.RIGHT, y):
            xy[0] = x + c.RIGHT
            xy[1] = y
        elif self._game.legal_field(x, y, 0, c.UP, 1) and not self._game.collide(0, False, x, y + c.UP):
            xy[0] = x
            xy[1] = y + c.UP
        elif self._game.legal_field(x, y, 0, c.DOWN, 1) and not self._game.collide(0, False, x, y + c.DOWN):
            xy[0] = x
            xy[1] = y + c.DOWN
        elif (not sawing or self._game.hex_board) and self._game.legal_field(x, y, c.LEFT, c.UP, 1) and not self._game.collide(0, False, x + c.LEFT, y + c.UP):
            xy[0] = x + c.LEFT
            xy[1] = y + c.UP
        elif (not sawing or self._game.hex_board) and self._game.legal_field(x, y, c.RIGHT, c.DOWN, 1) and not self._game.collide(0, False, x + c.RIGHT, y + c.DOWN):
            xy[0] = x + c.RIGHT
            xy[1] = y + c.DOWN
        elif not sawing and not self._game.hex_board and self._game.legal_field(x, y, c.RIGHT, c.UP, 1) and not self._game.collide(0, False, x + c.RIGHT, y + c.UP):
            xy[0] = x + c.RIGHT
            xy[1] = y + c.UP
        elif not sawing and not self._game.hex_board and self._game.legal_field(x, y, c.LEFT, c.DOWN, 1) and not self._game.collide(0, False, x + c.LEFT, y + c.DOWN):
            xy[0] = x + c.LEFT
            xy[1] = y + c.DOWN

    def collide(self, current_spiece, act_if_collide, x, y):
        for spiece in self.__organisms:
            if spiece.Get_X() == x and spiece.Get_Y() == y:
                if act_if_collide:
                    return self.__organisms[current_spiece].collidion(current_spiece, spiece)
                else:
                    return True

        return False
    def make_turn(self, key):
        self.__key = key
        self.__turn += 1
        self.__MainWindow.add_message(f"Turn nr: {self.__turn}")
        print("Turn nr: " + str(self.__turn))
        print("Size: " + str(self.__size))
        self.__size_at_begining = self.__size
        for organism in self.__organisms:
            organism.IncreaseAge()
            organism.SetMoved(False)

        for current in range(self.__size_at_begining):
            while not self.__organisms[current].GetMoved():
                self.__organisms[current].Action(current)

    def add_organism(self, new_organism):
        self.__MainWindow.add_message(f"New Organism:")
        if self.__size < c.MAX_NR_OF_ORGANISMS:
            self.__organisms.append(new_organism)
            self.__size += 1
        else:
            print("The world is full. Cannot add more organisms.")

    def add_organims_to_cell(self, canvas, x, y, xy):
        xy = xy - 1
        menu = tk.Menu(canvas, tearoff=0)
        menu.add_command(label="Wolf", command=lambda: self.handle_option("Wolf", xy))
        menu.add_command(label="Sheep", command=lambda: self.handle_option("Sheep", xy))
        menu.add_command(label="Fox", command=lambda: self.handle_option("Fox", xy))
        menu.post(x, y)

    def handle_option(self, option, xy):
        x = xy % c.GRID_SIZE
        y = int((xy - x)/ c.GRID_SIZE)
        if option == "Wolf":
            wolf = Wolf(self, 1, x, y)
            self.add_organism(wolf)

    def message(self, message):
        self.__MainWindow.add_message(message)

    # Getter methods for private variables
    def get_organisms(self):
        return self.__organisms

    def get_organism(self, id):
        return self.__organisms[id]
    def is_hex(self):
        return self.__is_hex

    def get_list_of_organisms(self):
        return self.__list_of_organisms

    def get_size(self):
        return self.__size

    def get_turn(self):
        return self.__turn


