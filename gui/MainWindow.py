import tkinter as tk
from const import constants

from gui.HexGrid import HexagonalGrid
from gui.SquareGrid import SquareGrid

from game.World import World
from game.Wolf import Wolf


class MainWindow:
    def __init__(self):
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
        self.__key = event.keysym
        print(message)
        self.add_message(message)

    def create_hexagonal_grid(self):
        self.__ishex = True
        self.__canvas.delete("all")
        self.__grid = HexagonalGrid(self.__canvas, constants.GRID_SIZE, constants.HEX_SIZE, self.__game)
        self.__canvas.bind("<Button-1>", lambda event: self.on_mouse_click(event, self.__grid))

    def create_square_grid(self):
        self.__ishex = False
        self.__canvas.delete("all")
        self.__grid = SquareGrid(self.__canvas, constants.GRID_SIZE, constants.SQUARE_SIZE, self.__game)
        self.__canvas.bind("<Button-1>", lambda event: self.on_mouse_click(event, self.__grid))

    def load_game(self):
        self.add_message("Game is loading...")

    def new_game(self):
        wolf = Wolf(self.__game, 8, 4, 5)
        self.__game.add_organism(wolf)
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
