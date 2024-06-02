import random
from const.constants import *
from game.Plant import Plant

class Belladonna(Plant):
    def __init__(self, game, age=None, position_X=None, position_Y=None,  strength=None, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
            strength = 99
        elif age is not None and position_X is not None and position_Y is not None:
            if strength is None:
                strength = 99
        else:
            raise ValueError("Invalid constructor parameters for Belladonna.")

        super().__init__(game, strength=strength,  age=age, position_X=position_X,
                         position_Y=position_Y, symbol="b")

    def baby(self, x, y):
        baby = Belladonna(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True

    def basic_fight(self, my_id, attacker_id):
        self._game.message(f"Fight: {self._game.get_organism(attacker_id).get_symbol()} vs {self._symbol}")
        self._game.message("Both died")
        self._game.get_organism(attacker_id).set_dead(True)
        self.set_dead(True)
        return False
