import random
from const.constants import *
from game.Animal import Animal

class Cyber_sheep(Animal):
    def __init__(self, game, age=None, position_X=None, position_Y=None, strength=11, initiative=4, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
        elif age is not None and position_X is not None and position_Y is not None:
            if initiative is None:
                initiative = 4
        else:
            raise ValueError("Invalid constructor parameters for Cyber_sheep.")

        super().__init__(game, strength=strength, initiative=initiative, age=age, position_X=position_X,
                         position_Y=position_Y, symbol="C")

    def baby(self, xy):
        baby = Cyber_sheep(self._game, xy=xy)
        self._game.add_organism(baby)
        self._moved = True

    def basic_way_to_weed(self, my_id, hogweed_x, hogweed_y):
        if hogweed_x > self._X:
            if not self._game.collide(my_id, True, self._X + RIGHT, self._Y):
                self.move(RIGHT, 0, 1)
        elif hogweed_x < self._X:
            if not self._game.collide(my_id, True, self._X + LEFT, self._Y):
                self.move(LEFT, 0, 1)
        elif hogweed_y < self._Y:
            if not self._game.collide(my_id, True, self._X, self._Y + UP):
                self.move(0, UP, 1)
        elif hogweed_y > self._Y:
            if not self._game.collide(my_id, True, self._X, self._Y + DOWN):
                self.move(0, DOWN, 1)

    def action(self, my_id):
        closest_hogweed = None
        distance = BOARD_SIZE + BOARD_SIZE + 1
        for i in range(self._game.get_size()):
            organism = self._game.get_organism(i)
            if organism.get_symbol() == sosnowsky_symbol:
                if not self._game.is_hex():
                    x = abs(self._X - organism.get_x())
                    y = abs(self._Y - organism.get_y())
                    tmp = x + y
                    if tmp < distance:
                        distance = tmp
                        closest_hogweed = organism
                else:
                    x = self._X - organism.get_x()
                    y = self._Y - organism.get_y()
                    tmp = 0
                    if x < 0 and y < 0:
                        while x < 0 and y < 0:
                            tmp += 1
                            x += 1
                            y += 1
                        tmp += abs(x) + abs(y)
                    elif x > 0 and y > 0:
                        while x > 0 and y > 0:
                            tmp += 1
                            x -= 1
                            y -= 1
                        tmp += abs(x) + abs(y)
                    else:
                        tmp = abs(x) + abs(y)
                    if tmp < distance:
                        distance = tmp
                        closest_hogweed = organism

        if closest_hogweed is None:
            self.make_a_move(my_id, 1)
        else:
            if not self._game.is_hex():
                hogweed_x = closest_hogweed.get_x()
                hogweed_y = closest_hogweed.get_y()
                self.basic_way_to_weed(my_id, hogweed_x, hogweed_y)
            else:
                x = closest_hogweed.get_x() - self._X
                y = closest_hogweed.get_y() - self._Y
                if x > 0 and y > 0:
                    if not self._game.collide(my_id, True, self._X + RIGHT, self._Y + DOWN):
                        self.move(RIGHT, DOWN, 1)
                elif x < 0 and y < 0:
                    if not self._game.collide(my_id, True, self._X + LEFT, self._Y + UP):
                        self.move(LEFT, UP, 1)
                else:
                    self.basic_way_to_weed(my_id, closest_hogweed.get_x(), closest_hogweed.get_y())
