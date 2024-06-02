import random
from const import constants as c
from game.Organism import Organism

class Animal(Organism):
    def __init__(self, game, strength, initiative, age, position_X, position_Y, symbol):
        super().__init__(game, strength, initiative, age, position_X, position_Y, symbol, animal=True)

    #@abstractmethod
    def baby(self, x, y):
        pass

    def collision(self, my_id, defender_id):
        defender = self._game.get_organism(defender_id)
        if self._symbol == defender.get_symbol():
            self._moved = True
            if not defender.get_moved():
                defender.set_moved(True)
                xy = [-1, -1]
                self._game.search_for_free_space(xy, self._X, self._Y, False)
                if xy[0] == -1:
                    self._game.search_for_free_space(xy, defender.get_x(), defender.get_y(), False)
                if xy[0] == -1:
                    return True
                else:
                    self._game.message(f"New Organism: {self._symbol}")
                    self.baby(xy[0], xy[1])
                    return True
            return True
        else:
            self._moved = True
            return defender.fight(defender_id, my_id)

    def can_move_safely(self, x, y):
        for i in range(self._game.get_size()):
            organism = self._game.get_organism(i)
            if x == organism.get_x() and y == organism.get_y():
                if self._strength >= organism.get_strength():
                    return True
                else:
                    return False
        return True

    def is_there_option_to_move_safely(self):
        return (
            self.can_move_safely(self._X + c.LEFT, self._Y) or
            self.can_move_safely(self._X, self._Y + c.UP) or
            self.can_move_safely(self._X + c.RIGHT, self._Y) or
            self.can_move_safely(self._X, self._Y + c.DOWN) or
            (self._game.is_hex() and self.can_move_safely(self._X + c.LEFT, self._Y + c.UP)) or
            (self._game.is_hex() and self.can_move_safely(self._X + c.RIGHT, self._Y + c.DOWN))
        )

    def make_a_move(self, my_id, speed):
        roll = random.randint(1, 6)
        if roll == 1:
            if not self._game.collide(my_id, True, self._X + c.LEFT * speed, self._Y):
                self.move(c.LEFT * speed, 0, speed)
        elif roll == 2:
            if not self._game.collide(my_id, True, self._X, self._Y + c.UP * speed):
                self.move(0, c.UP * speed, speed)
        elif roll == 3:
            if not self._game.collide(my_id, True, self._X + c.RIGHT * speed, self._Y):
                self.move(c.RIGHT * speed, 0, speed)
        elif roll == 4:
            if not self._game.collide(my_id, True, self._X, self._Y + c.DOWN * speed):
                self.move(0, c.DOWN * speed, speed)
        elif roll == 5 and self._game.is_hex():
            if not self._game.collide(my_id, True, self._X + c.LEFT * speed, self._Y + c.UP * speed):
                self.move(c.LEFT * speed, c.UP * speed, speed)
        elif roll == 6 and self._game.is_hex():
            if not self._game.collide(my_id, True, self._X + c.RIGHT * speed, self._Y + c.DOWN * speed):
                self.move(c.RIGHT * speed, c.DOWN * speed, speed)

    def action(self, my_id):
        self.make_a_move(my_id, 1)
