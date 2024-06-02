from dataclasses import dataclass
from game.Plant import Plant

@dataclass
class Grass(Plant):
    def __init__(self, game, age=None, position_X=None, position_Y=None, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
            initiative = 0
        elif age is not None and position_X is not None and position_Y is not None:
            k = 6
        else:
            raise ValueError("Invalid constructor parameters for Grass.")

        super().__init__(game, strength=0, age=age, position_X=position_X, position_Y=position_Y, symbol="''")

    def baby(self, x, y):
        baby = Grass(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True
