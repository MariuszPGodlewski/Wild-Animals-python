from const import constants as c
import tkinter as tk

from game.Human import Human

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

class World:
    def __init__(self, MainWindow):
        self.__organisms = []
        self.__is_hex = False
        self.__list_of_organisms = ["Wolf", "Sheep", "Fox", "Turtle", "Antelope", "Cyber_sheep", "Grass", "Thistle", "Guarana", "Belladonna", "Sosnowsky_hogweed"]
        self.__size = 0
        self.__size_at_beginning = 0
        self.__turn = 0
        self.__MainWindow = MainWindow
        #self.__key = ""
        print("World created")

    def legal_field(self, current_x, current_y, direction_x, direction_y, speed):
        new_x = current_x + (direction_x * speed)
        new_y = current_y + (direction_y * speed)
        return 0 <= new_x < c.GRID_SIZE and 0 <= new_y < c.GRID_SIZE

    def collide(self, current_species, act_if_collide, x, y):
        for spiece in range(self.__size):
            species = self.__organisms[spiece]
            if not species.is_dead() and species.get_x() == x and species.get_y() == y:
                if act_if_collide:
                    return self.__organisms[current_species].collision(current_species, spiece)
                else:
                    return True
        return False

    def search_for_free_space(self, xy, x, y, sawing):
        xy[0] = -1
        xy[1] = -1
        directions = [(c.LEFT, 0), (c.RIGHT, 0), (0, c.UP), (0, c.DOWN)]
        if not sawing or self.__is_hex:
            directions += [(c.LEFT, c.UP), (c.RIGHT, c.DOWN)]
        if not sawing and not self.__is_hex:
            directions += [(c.RIGHT, c.UP), (c.LEFT, c.DOWN)]

        for dx, dy in directions:
            if self.legal_field(x, y, dx, dy, 1) and not self.collide(0, False, x + dx, y + dy):
                xy[0] = x + dx
                xy[1] = y + dy
                break

    def remove_dead(self):
        i = 0
        while i < self.__size:
            organism = self.__organisms[i]
            if organism.is_dead():
                # Shift elements to the left to fill the gap
                for j in range(i, self.__size - 1):
                    self.__organisms[j] = self.__organisms[j + 1]
                self.__organisms[self.__size - 1] = None
                self.__size -= 1
            else:
                i += 1
        # Optionally, resize the list to remove None elements at the end
        self.__organisms = self.__organisms[:self.__size]

    def sort_organisms(self):
        for i in range(self.__size - 1):
            for j in range(self.__size - i - 1):
                # Compare by initiative first
                if self.__organisms[j].get_initiative() != self.__organisms[j + 1].get_initiative():
                    # Sort by initiative in descending order
                    if self.__organisms[j].get_initiative() < self.__organisms[j + 1].get_initiative():
                        self.__organisms[j], self.__organisms[j + 1] = self.__organisms[j + 1], self.__organisms[j]
                else:  # If initiative is equal, compare by age
                    # Sort by age in descending order
                    if self.__organisms[j].get_age() < self.__organisms[j + 1].get_age():
                        self.__organisms[j], self.__organisms[j + 1] = self.__organisms[j + 1], self.__organisms[j]

    def make_turn(self, key):
        self.sort_organisms()
        self.__key = key
        self.__turn += 1
        self.__MainWindow.add_message(f"Turn nr: {self.__turn}")
        print(f"Turn nr: {self.__turn}")
        print(f"Size: {self.__size}")
        self.__size_at_beginning = self.__size

        for organism in self.__organisms:
            organism.age_increase()
            organism.set_moved(False)

        for current in range(self.__size_at_beginning):
            if not self.__organisms[current].is_dead():
                while not self.__organisms[current].get_moved():
                    self.__organisms[current].action(current)

        self.remove_dead()
        self.sort_organisms()

    def add_organism(self, new_organism):
        self.__MainWindow.add_message("New Organism added.")
        if self.__size < c.MAX_NR_OF_ORGANISMS:
            self.__organisms.append(new_organism)
            self.__size += 1
        else:
            print("The world is full. Cannot add more organisms.")

    def add_organism_to_cell(self, canvas, x, y, xy):
        xy = xy - 1
        menu = tk.Menu(canvas, tearoff=0)
        for organism in self.__list_of_organisms:
            menu.add_command(label=organism, command=lambda option=organism: self.handle_option(option, xy))
        menu.post(x, y)

    def handle_option(self, option, xy):
        x = xy % c.GRID_SIZE
        y = xy // c.GRID_SIZE
        if option == "Wolf":
            wolf = Wolf(self, xy=[x, y])
            self.add_organism(wolf)
        elif option == "Sheep":
            animal = Sheep(self, xy=[x, y])
            self.add_organism(animal)
        # Add other organism handling as needed

    def message(self, message):
        self.__MainWindow.add_message(message)

    # Getter methods for private variables

    def get_key(self):
        return self.__key

    def get_organisms(self):
        return self.__organisms

    def remove_organism(self, id):
        if 0 <= id < self.__size:
            self.__organisms[id].set_dead(True)

    def get_organism(self, index):
        index = int(index)
        if 0 <= index < self.__size:
            return self.__organisms[index]
        else:
            return None

    def is_hex(self):
        return self.__is_hex

    def set_hex(self, is_it):
        self.__is_hex = is_it

    def get_list_of_organisms(self):
        return self.__list_of_organisms

    def abiliety_h(self):
        for spiece in self.__organisms:
            if spiece.get_symbol() == "H":
                spiece.power()

    def get_size(self):
        return self.__size

    def get_turn(self):
        return self.__turn

    def save_game(self):
        filename = "Wield_animals_save.txt"

        try:
            with open(filename, 'w') as file:
                file.write(f"{self.__is_hex}\n")
                file.write(f"{self.__size}\n")
                for organism in self.__organisms:
                    file.write(
                        f"{organism.get_symbol()} "
                        f"{organism.get_initiative()} "
                        f"{organism.get_age()} "
                        f"{organism.get_strength()} "
                        f"{organism.get_x()} "
                        f"{organism.get_y()}"
                    )
                    if organism.get_symbol() != "H":
                        file.write("\n")
                    else:
                        abilities = organism.get_abilities()
                        file.write(f" {abilities[0]} {abilities[1]}\n")
            print(f"Data has been written to {filename}")
        except IOError as e:
            print(f"An error occurred: {e}")
            raise

    def load_save(self):
        filename = "Wield_animals_save.txt"

        try:
            with open(filename, 'r') as file:
                self.__is_hex = file.readline().strip().lower() == 'true'
                print(self.is_hex())

                save_size = int(file.readline().strip())
                print(save_size)

                self.__organisms = []
                for _ in range(save_size):
                    line = file.readline().strip()
                    print(line)
                    parts = line.split()
                    symbol = parts[0]
                    initiative = int(parts[1])
                    age = int(parts[2])
                    strength = int(parts[3])
                    x = int(parts[4])
                    y = int(parts[5])
                    abilities = (int(parts[6]), int(parts[7])) if symbol == "H" else None

                    organism = self.create_organism(symbol, initiative, age, strength, x, y, abilities)
                    self.add_organism(organism)

        except IOError as e:
            print(f"An error occurred: {e}")
            raise

    def create_organism(self, symbol, initiative, age, strength, x, y, abilities=None):
        if symbol == "H":
            return Human(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength,abilities=abilities)
            #return Human(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength, if abilities is None else (abilities[0], abilities[1]))
        elif symbol == "W":
            return Wolf(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength, xy=None)
        elif symbol == "S":
            return Sheep(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength, xy=None)
        elif symbol == "F":
            return Fox(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength, xy=None)
        elif symbol == "T":
            return Turtle(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength, xy=None)
        elif symbol == "A":
            return Antelope(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength,xy=None)
        elif symbol == "C":
            return Cyber_sheep(self, age=age, position_X=x, position_Y=y, initiative=initiative, strength=strength,xy=None)
        elif symbol == "''":
            return Grass(self, age=age, position_X=x, position_Y=y, xy=None)
        elif symbol == "t":
            return Thistle(self, age=age, position_X=x, position_Y=y,xy=None)
        elif symbol == "g":
            return Guarana(self, age=age, position_X=x, position_Y=y,xy=None)
        elif symbol == "b":
            return Belladonna(self, age=age, position_X=x, position_Y=y,xy=None)
        elif symbol == "s":
            return Sosnowsky_hogweed(self, age=age, position_X=x, position_Y=y, xy=None)
        else:
            raise ValueError(f"Unknown symbol: {symbol}")
