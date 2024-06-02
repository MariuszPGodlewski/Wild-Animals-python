from dataclasses import dataclass
from game.Plant import Plant
import random

@dataclass
class Thistle(Plant):
    NR_OF_SAWING: int = 3

    def __init__(self, game, age=None, position_X=None, position_Y=None, initiative=0, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
            initiative = 0
        elif age is not None and position_X is not None and position_Y is not None:
            if initiative is None:
                initiative = 0
        else:
            raise ValueError("Invalid constructor parameters for Thistle.")

        super().__init__(game, strength=0, age=age, position_X=position_X, position_Y=position_Y, symbol="t")

    def action(self, my_id):
        for _ in range(self.NR_OF_SAWING):
            self.sawing(my_id)

    def baby(self, x, y):
        baby = Thistle(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True
