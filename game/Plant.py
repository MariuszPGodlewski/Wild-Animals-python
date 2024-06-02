import random
from const.constants import *
from game.Organism import Organism

class Plant(Organism):
    SAWING_CHANCE = 10

    def __init__(self, game, strength, age, position_X, position_Y, symbol):
        super().__init__(game, strength, 0, age, position_X, position_Y, symbol, False)

    def baby(self, x, y):
        raise NotImplementedError("This method should be overridden by subclasses")

    def sawing(self, my_id):
        saw_roll = random.randint(0, 99)

        xy = [0, 0]
        self._game.search_for_free_space(xy, self._X, self._Y, True)
        if xy[0] == -1:
            self._moved = True

        if not self._moved and saw_roll < SAWING_CHANCE:
            roll = random.randint(1, 6)
            if roll == 1:
                if self._game.legal_field(self._X, self._Y, LEFT, 0, 1) and not self._game.collide(my_id, False, self._X + LEFT, self._Y):
                    self.baby(self._X + LEFT, self._Y)
            elif roll == 2:
                if self._game.legal_field(self._X, self._Y, 0, UP, 1) and not self._game.collide(my_id, False, self._X, self._Y + UP):
                    self.baby(self._X, self._Y + UP)
            elif roll == 3:
                if self._game.legal_field(self._X, self._Y, RIGHT, 0, 1) and not self._game.collide(my_id, False, self._X + RIGHT, self._Y):
                    self.baby(self._X + RIGHT, self._Y)
            elif roll == 4:
                if self._game.legal_field(self._X, self._Y, 0, DOWN, 1) and not self._game.collide(my_id, False, self._X,self._Y + DOWN):
                    self.baby(self._X, self._Y + DOWN)
            elif roll == 5 and self._game.is_hex():
                if self._game.legal_field(self._X, self._Y, LEFT, UP, 1) and not self._game.collide(my_id, False, self._X + LEFT,self._Y + UP):
                    self.baby(self._X + LEFT, self._Y + UP)
            elif roll == 6 and self._game.is_hex():
                if self._game.legal_field(self._X, self._Y, RIGHT, DOWN, 1) and not self._game.collide(my_id, False, self._X + RIGHT, self._Y + DOWN):
                    self.baby(self._X + RIGHT, self._Y + DOWN)

            if self._moved:
                self._game.message(f"Sawd: {self._symbol}")
        else:
            self._moved = True

    def action(self, my_id):
        self.sawing(my_id)

    def collision(self, my_id, defender_id):
        return False
