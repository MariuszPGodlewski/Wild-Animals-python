from dataclasses import dataclass
from game.Animal import Animal

@dataclass
class Sheep(Animal):
    def __init__(self, game, age=None, position_X=None, position_Y=None, initiative=None, strength=None, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
            initiative = 4
            strength = 4
        elif age is not None and position_X is not None and position_Y is not None:
            if initiative is None:
                initiative = 4
            if strength is None:
                strength = 4
        else:
            raise ValueError("Invalid constructor parameters for Sheep.")

        super().__init__(game, strength=strength, initiative=initiative, age=age, position_X=position_X,
                         position_Y=position_Y, symbol="S")

    def baby(self, x, y):
        baby = Sheep(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True
