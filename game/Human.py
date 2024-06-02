import random
from game.Animal import Animal
from const.constants import *

class Human(Animal):
    def __init__(self, game, age=1, position_X=0, position_Y=0, initiative=5, strength=4, abilities=None):
        super().__init__(game,  strength=strength, initiative=initiative, age=age, position_X=position_X, position_Y=position_Y, symbol="H", )
        self._speed = 1
        self._bonus_duration = 0
        self._symbol = "H"
        if abilities:
            self._bonus_duration = abilities[1]
            self._speed = abilities[0]

    def action(self, my_id):
        direction = self._game.get_key()

        if direction == "f":
            if not self._game.collide(my_id, True, self._X + LEFT * self._speed, self._Y):
                self.move(LEFT * self._speed, 0, self._speed)
        elif direction == "y":
            if not self._game.collide(my_id, True, self._X, self._Y + UP * self._speed):
                self.move(0, UP * self._speed, self._speed)
        elif direction == "h":
            if not self._game.collide(my_id, True, self._X + RIGHT * self._speed, self._Y):
                self.move(RIGHT * self._speed, 0, self._speed)
        elif direction == "b":
            if not self._game.collide(my_id, True, self._X, self._Y + DOWN * self._speed):
                self.move(0, DOWN * self._speed, self._speed)
        elif direction == "t" and self._game.is_hex():
            if not self._game.collide(my_id, True, self._X + LEFT * self._speed, self._Y + UP * self._speed):
                self.move(LEFT * self._speed, UP * self._speed, self._speed)
        elif direction == "v" and self._game.is_hex():
            if not self._game.collide(my_id, True, self._X + RIGHT * self._speed, self._Y + DOWN * self._speed):
                self.move(RIGHT * self._speed, DOWN * self._speed, self._speed)

        self.set_moved(True)

        if self._moved:
            if self._bonus_duration == 0:
                self._speed = 1
            elif 1 <= self._bonus_duration < 3:
                roll = random.randint(1, 2)
                self._speed = 2 if roll == 1 else 1

            if self._bonus_duration > 0:
                self._bonus_duration -= 1

    def power(self):
        if self._bonus_duration == 0:
            self._bonus_duration = 4
            self._speed = 2

    def baby(self, x, y):
        baby_human = Human(self._game, position_X=x, position_Y=y)
        self._game.add_organism(baby_human)
        self._moved = True

    def get_abilities(self):
        return [self._speed, self._bonus_duration]
