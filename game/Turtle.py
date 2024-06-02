from dataclasses import dataclass
import random
from game.Animal import Animal

@dataclass
class Turtle(Animal):
    TURTLE_REFLECTION: int = 5

    def __init__(self, game, age=None, position_X=None, position_Y=None, initiative=None, strength=None, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
            initiative = 1
            strength = 2
        elif age is not None and position_X is not None and position_Y is not None:
            if initiative is None:
                initiative = 1
            if strength is None:
                strength = 2
        else:
            raise ValueError("Invalid constructor parameters for Turtle.")

        super().__init__(game, strength=strength, initiative=initiative, age=age, position_X=position_X,
                         position_Y=position_Y, symbol="T")

    def basic_fight(self, my_id, attacker_id):
        self._game.message(f"Fight: {self._game.get_organism(attacker_id).get_symbol()} vs {self._symbol}")
        attacker_strength = self._game.get_organism(attacker_id).get_strength()
        if attacker_strength <= self.TURTLE_REFLECTION:
            self._game.message(f"Turtle reflected the attack")
            self._game.get_organism(attacker_id).set_moved(True)
            return True
        else:
            if self._game.get_organism(attacker_id).get_strength() >= self._strength:
                self._game.remove_organism(my_id)
                self._game.message(f"Won: {self._game.get_organism(attacker_id).get_symbol()}")
                return False
            self._game.message(f"Won: {self._symbol}")
            self._game.remove_organism(attacker_id)
            return True

    def action(self, my_id):
        roll = random.randint(1, 4)
        if roll == 1:
            self.make_a_move(my_id, 1)
        else:
            self._moved = True

    def baby(self, x, y):
        baby = Turtle(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True
