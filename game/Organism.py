from abc import ABC, abstractmethod
from const import constants as c

class Organism(ABC):
    def __init__(self, game, strength, initiative, age, position_X, position_Y, symbol, animal):
        self._game = game
        self._strength = strength
        self._initiative = initiative
        self._age = age
        self._X = position_X
        self._Y = position_Y
        self._symbol = symbol
        self._moved = False
        self._animal = animal
        self._dead = False

    @abstractmethod
    def action(self, my_id):
        pass

    @abstractmethod
    def collision(self, my_id, defender_id):
        pass

    def power(self):
        pass

    def set_dead(self, is_dead):
        self._dead = is_dead

    def is_dead(self):
        return self._dead
    def basic_fight(self, my_id, attacker_id):
        self._game.message(f"Fight: {self._game.get_organism(attacker_id).get_symbol()} vs {self._symbol}")
        if self._game.get_organism(attacker_id).get_strength() >= self._strength:
            self._game.remove_organism(my_id)
            self._game.message(f"Won: {self._game.get_organism(attacker_id).get_symbol()}")
            return False
        self._game.message(f"Won: {self._symbol}")
        self._game.remove_organism(attacker_id)
        return True

    def fight(self, my_id, attacker_id):
        return self.basic_fight(my_id, attacker_id)

    def get_strength(self):
        return self._strength

    def strength_adjustment(self, bonus):
        self._strength += bonus

    def get_initiative(self):
        return self._initiative

    def set_initiative(self, initiative):
        self._initiative = initiative

    def get_age(self):
        return self._age

    def age_increase(self):
        self._age += 1

    def get_x(self):
        return self._X

    def set_x(self, position_X):
        self._X = position_X

    def get_y(self):
        return self._Y

    def set_y(self, position_Y):
        self._Y = position_Y

    def get_symbol(self):
        return self._symbol

    def get_moved(self):
        return self._moved

    def set_moved(self, moved):
        self._moved = moved

    def is_animal(self):
        return self._animal

    def move(self, move_x, move_y, speed):
        if move_x == c.LEFT * speed and move_y == 0 and self._X >= 1 * speed:
            self._X += c.LEFT * speed
            self._moved = True
        elif move_x == c.RIGHT * speed and move_y == 0 and self._X < c.BOARD_SIZE - 1 * speed:
            self._X += c.RIGHT * speed
            self._moved = True
        elif move_x == 0 and move_y == c.UP * speed and self._Y >= 1 * speed:
            self._Y += c.UP * speed
            self._moved = True
        elif move_x == 0 and move_y == c.DOWN * speed and self._Y < c.BOARD_SIZE - 1 * speed:
            self._Y += c.DOWN * speed
            self._moved = True
        elif move_x == c.LEFT * speed and move_y == c.UP * speed and self._X >= 1 * speed and self._Y >= 1 * speed:
            self._X += c.LEFT * speed
            self._Y += c.UP * speed
            self._moved = True
        elif move_x == c.RIGHT * speed and move_y == c.DOWN * speed and self._X < c.BOARD_SIZE - 1 * speed and self._Y < c.BOARD_SIZE - 1 * speed:
            self._X += c.RIGHT * speed
            self._Y += c.DOWN * speed
            self._moved = True
