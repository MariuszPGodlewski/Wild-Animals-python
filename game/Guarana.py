from dataclasses import dataclass
from game.Plant import Plant

@dataclass
class Guarana(Plant):
    BONUS_STRENGTH: int = 3

    def __init__(self, game, age=None, position_X=None, position_Y=None, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
        elif age is not None and position_X is not None and position_Y is not None:
            k=7
        else:
            raise ValueError("Invalid constructor parameters for Guarana.")

        super().__init__(game, strength=0,  age=age, position_X=position_X,
                         position_Y=position_Y, symbol="g")

    def baby(self, x, y):
        baby = Guarana(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True

    def basic_fight(self, my_id, attacker_id):
        attacker = self._game.get_organism(attacker_id)
        attacker.strength_adjustment(self.BONUS_STRENGTH)

        self._game.message(f"Fight: {self._game.get_organism(attacker_id).get_symbol()} vs {self._symbol}")
        if self._game.get_organism(attacker_id).get_strength() >= self._strength:
            self._game.remove_organism(my_id)
            self._game.message(f"Won: {self._game.get_organism(attacker_id).get_symbol()}")
            return False
        self._game.message(f"Gets strength bonus: {self._symbol}")
        self._game.remove_organism(attacker_id)
        return True
