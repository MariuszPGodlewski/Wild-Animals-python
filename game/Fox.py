from dataclasses import dataclass
import random
from game.Animal import Animal
from const.constants import *
@dataclass
class Fox(Animal):
    def __init__(self, game, age=None, position_X=None, position_Y=None, initiative=None, strength=None, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
            initiative = 7
            strength = 3
        elif age is not None and position_X is not None and position_Y is not None:
            if initiative is None:
                initiative = 7
            if strength is None:
                strength = 3
        else:
            raise ValueError("Invalid constructor parameters for Fox.")

        super().__init__(game, strength=strength, initiative=initiative, age=age, position_X=position_X,
                         position_Y=position_Y, symbol="F")

    def action(self, my_id):
        if not self.is_there_option_to_move_safely():
            self._moved = True
        else:
            roll = random.randint(1, 6)
            if roll == 1:
                if self.can_move_safely(self._X + LEFT, self._Y) and not self._game.collide(my_id, True, self._X + LEFT, self._Y):
                    self.move(LEFT, 0, 1)
                    self._moved = True
            elif roll == 2:
                if self.can_move_safely(self._X, self._Y + UP) and \
                        not self._game.collide(my_id, True, self._X, self._Y + UP):
                    self.move(0, UP, 1)
                    self._moved = True
            elif roll == 3:
                if self.can_move_safely(self._X + RIGHT, self._Y) and \
                        not self._game.collide(my_id, True, self._X + RIGHT, self._Y):
                    self.move(RIGHT, 0, 1)
                    self._moved = True
            elif roll == 4:
                if self.can_move_safely(self._X, self._Y + DOWN) and \
                        not self._game.collide(my_id, True, self._X, self._Y + DOWN):
                    self.move(0, DOWN, 1)
                    self._moved = True
            elif roll == 5 and self._game.is_hex():
                if self.can_move_safely(self._X + LEFT, self._Y + UP) and \
                        not self._game.collide(my_id, True, self._X + LEFT, self._Y + UP):
                    self.move(LEFT, UP, 1)
                    self._moved = True
            elif roll == 6 and self._game.is_hex():
                if self.can_move_safely(self._X + RIGHT, self._Y + DOWN) and \
                        not self._game.collide(my_id, True, self._X + RIGHT, self._Y + DOWN):
                    self.move(RIGHT, DOWN, 1)
                    self._moved = True

    def baby(self, x, y):
        baby = Fox(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True
