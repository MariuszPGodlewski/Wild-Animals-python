from game.Plant import Plant
from const.constants import *

class Sosnowsky_hogweed(Plant):
    def __init__(self, game, age=None, position_X=None, position_Y=None, xy=None):
        if xy is not None:
            position_X, position_Y = xy
            age = 1
        elif age is not None and position_X is not None and position_Y is not None:
            p = 4
        else:
            raise ValueError("Invalid constructor parameters for Sosnowsky_hogweed.")

        super().__init__(game, strength=10, age=age, position_X=position_X,
                         position_Y=position_Y, symbol="s")

    def baby(self, x, y):
        baby = Sosnowsky_hogweed(self._game, xy=[x, y])
        self._game.add_organism(baby)
        self._moved = True

    def action(self, my_id):
        # kill the neighbors
        for i in range(self._game.get_size()):
            organism = self._game.get_organism(i)
            if organism.is_animal() and organism.get_symbol() != cybersheep_symbol:
                if (self._X + LEFT == organism.get_x() and self._Y == organism.get_y() or
                        self._X + RIGHT == organism.get_x() and self._Y == organism.get_y() or
                        self._X == organism.get_x() and self._Y + DOWN == organism.get_y() or
                        self._X == organism.get_x() and self._Y + UP == organism.get_y() or
                        (
                                self._game.is_hex() and self._X + LEFT == organism.get_x() and self._Y + UP == organism.get_y()) or
                        (
                                self._game.is_hex() and self._X + RIGHT == organism.get_x() and self._Y + DOWN == organism.get_y())):
                    self._game.message(f"Sosnowsky killed: {organism.get_symbol()}")
                    organism.set_dead(True)

        self.sawing(my_id)

    def basic_fight(self, my_id, attacker_id):
        attacker = self._game.get_organism(attacker_id)
        self._game.message(f"Fight: {attacker.get_symbol()} vs {self._symbol}")

        if attacker.is_animal() and attacker.get_symbol() != cybersheep_symbol:
            self._game.message("Both died")
            self.set_dead(True)
            attacker.set_dead(True)
            return False
        elif attacker.get_symbol() == cybersheep_symbol:
            self._game.message("Cyber sheep ate hogweed")
            self.set_dead(True)
            return False

        self._game.message(f"Fight: {self._game.get_organism(attacker_id).get_symbol()} vs {self._symbol}")
        if self._game.get_organism(attacker_id).get_strength() >= self._strength:
            self._game.remove_organism(my_id)
            self._game.message(f"Won: {self._game.get_organism(attacker_id).get_symbol()}")
            return False
        self._game.message(f"Won: {self._symbol}")
        self._game.remove_organism(attacker_id)
        return True
