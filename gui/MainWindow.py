import tkinter as tk
from const import constants

from gui.HexGrid import HexagonalGrid
from gui.SquareGrid import SquareGrid

from game.Human import Human

from game.World import World

from game.Wolf import Wolf
from game.Sheep import Sheep
from game.Fox import Fox
from game.Turtle import Turtle
from game.Antelope import Antelope
from game.Cyber import Cyber_sheep

from game.Grass import Grass
from game.Thistle import Thistle
from game.Guarana import Guarana
from game.Belladonna import Belladonna
from game.Hogweed import Sosnowsky_hogweed

class MainWindow:
    def __init__(self):
        try:
            self.__root = tk.Tk()
            self.__root.title("Mariusz Godlewski")
            self.__key = ""
            self.__canvas = tk.Canvas(self.__root, width=700, height=500)
            self.__canvas.pack(side=tk.LEFT)
            menu = tk.Menu(self.__root)
            self.__root.config(menu=menu)
            self.__ishex = False
            self.__game = World(self)

            grid_menu = tk.Menu(menu, tearoff=0)
            menu.add_cascade(label="Grid Type", menu=grid_menu)
            grid_menu.add_command(label="Hexagonal", command=self.create_hexagonal_grid)
            grid_menu.add_command(label="Square", command=self.create_square_grid)

            load_menu = tk.Menu(menu, tearoff=0)
            menu.add_cascade(label="Game", menu=load_menu)
            load_menu.add_command(label="New game", command=self.new_game)
            load_menu.add_command(label="Save game", command=self.save_game)
            load_menu.add_command(label="Load game", command=self.load_game)

            message_frame = tk.Frame(self.__root)
            message_frame.pack(side=tk.TOP)

            self.clear_button = tk.Button(message_frame, text="Next Turn", command=self.next_turn)
            self.clear_button.pack(side=tk.LEFT)

            self.message_box = tk.Text(self.__root, height=50, width=20)
            self.message_box.pack(side=tk.TOP)
            self.message_box.config(state=tk.DISABLED)

            # Initialize message box with initial message
            self.initialize_message_box("Welcome to the application!")

            self.__root.bind("<KeyPress>", self.on_key_press)

            self.__root.mainloop()
        except KeyboardInterrupt:
            pass

    def add_message(self, message):
        self.message_box.config(state=tk.NORMAL)
        self.message_box.insert(tk.END, message + "\n")
        self.message_box.config(state=tk.DISABLED)

    def initialize_message_box(self, initial_message):
        self.add_message(initial_message)

    def on_mouse_click(self, event, grid):
        xy = grid.get_clicked(event.x, event.y)
        message = f"Clicked hexagon with ID: {xy}"
        print(message)
        self.add_message(message)
        if not self.__ishex:
            grid.on_click(event, int(xy))

    def on_key_press(self, event):
        message = f"Key pressed: {event.keysym}"
        if event.keysym == "s":
            self.__game.abiliety_h()
        self.__key = event.keysym
        print(message)
        self.add_message(message)

    def create_hexagonal_grid(self):
        self.__game.set_hex(True)
        self.__ishex = True
        self.__canvas.delete("all")
        self.__grid = HexagonalGrid(self.__canvas, constants.GRID_SIZE, constants.HEX_SIZE, self.__game)
        self.__canvas.bind("<Button-1>", lambda event: self.on_mouse_click(event, self.__grid))

    def create_square_grid(self):
        self.__game.set_hex(False)
        self.__ishex = False
        self.__canvas.delete("all")
        self.__grid = SquareGrid(self.__canvas, constants.GRID_SIZE, constants.SQUARE_SIZE, self.__game)
        self.__canvas.bind("<Button-1>", lambda event: self.on_mouse_click(event, self.__grid))

    def save_game(self):
        self.__game.save_game()

    def load_game(self):
        self.__game = World(self)
        self.__game.load_save()
        self.add_message("Game is loading...")
        if self.__game.is_hex():
            self.create_hexagonal_grid()
        else:
            self.create_square_grid()

    def new_game(self):
        self.__game = World(self)

        human = Human(self.__game, 12,  3, 4)
        self.__game.add_organism(human)
        wolf = Wolf(self.__game, 10, 9, 5)
        self.__game.add_organism(wolf)
        wolf = Wolf(self.__game, 0, 10, 5)
        self.__game.add_organism(wolf)
        turtle = Turtle(self.__game, 1, 5, 4)
        self.__game.add_organism(turtle)
        fox = Fox(self.__game, 4, 4, 4)
        self.__game.add_organism(fox)
        antelope = Antelope(self.__game, 7, 6, 6)
        self.__game.add_organism(antelope)
        cyber = Cyber_sheep(self.__game, 11, 11, 11)
        self.__game.add_organism(cyber)

        grass = Grass(self.__game, 3, 5, 5)
        self.__game.add_organism(grass)
        thistle = Thistle(self.__game, 1, 9, 9)
        self.__game.add_organism(thistle)
        guarana = Guarana(self.__game, 5, 3, 5)
        self.__game.add_organism(guarana)
        belladonna = Belladonna(self.__game, 2, 4, 1)
        self.__game.add_organism(belladonna)
        hoogweed = Sosnowsky_hogweed(self.__game, 2, 1, 1)
        self.__game.add_organism(hoogweed)

        self.add_message("New game")

    def next_turn(self):
        self.message_box.config(state=tk.NORMAL)  # Enable editing
        self.message_box.delete("1.0", tk.END)    # Delete all text
        self.message_box.config(state=tk.DISABLED)  # Disable editing
        self.__game.make_turn(self.__key)

        if self.__ishex:
            self.create_hexagonal_grid()
        else:
            self.create_square_grid()

    def get_world(self):
        return self.__game
