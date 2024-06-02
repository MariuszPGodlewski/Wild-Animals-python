from dataclasses import dataclass
import random
from game.Animal import Animal

@dataclass
class Antelope(Animal):
    ANTELOPE_SPEED: int = 2

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
            raise ValueError("Invalid constructor parameters for Antelope.")

        super().__init__(game, strength=strength, initiative=initiative, age=age, position_X=position_X,
                         position_Y=position_Y, symbol="A")

    def baby(self, x, y):
        baby = Antelope(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True

    def basic_fight(self, my_id, attacker_id):
        self._game.message(f"Fight: {self._game.get_organism(attacker_id).get_symbol()} vs {self._symbol}")
        roll = random.randint(1, 2)
        if roll == 1:
            self._game.message("Antelope run away")
            self._moved = False
            self.make_a_move(my_id, 2)
            return False
        else:
            if self._game.get_organism(attacker_id).get_strength() >= self._strength:
                self._game.remove_organism(my_id)
                self._game.message(f"Won: {self._game.get_organism(attacker_id).get_symbol()}")
                return False
            self._game.message(f"Won: {self._symbol}")
            self._game.remove_organism(attacker_id)
            return True

    def action(self, my_id):
        self.make_a_move(my_id, self.ANTELOPE_SPEED)
