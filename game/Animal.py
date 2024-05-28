import random
from const import constants as c
from game.Organism import Organism


class Animal(Organism):
    def __init__(self, game, strength, initiative, age, position_X, position_Y, symbol):
        super().__init__(game, strength, initiative, age, position_X, position_Y, symbol, animal=True)

    def collidion(self, my_id, defender_id):
        defender = self._game.get_organism(defender_id)
        if self._symbol == defender.GetSymbol():
            self._moved = True
            if not defender.GetMoved():
                defender.SetMoved(True)
                xy = [2]
                self._game.search_for_free_space(xy, self._X, self._Y, False)
                if xy[0] == -1:
                    self._game.search_for_free_space(xy, defender.Get_X, defender.Get_Y, False)
                if xy[0] == -1:
                    return True
                else:
                    self._game.add_message("New animal: " + self._symbol)
                    self.baby(xy[0], xy[1])
                    return True

    def Move(self, my_id, speed):
        roll = random.randint(1, 6)
        if roll == 1:
            if not self._game.collide(my_id, True, self._X + c.LEFT * speed, self._Y):
                if self._game.legal_field(self._X, self._Y, c.LEFT, 0, speed):
                    self.Set_X(self._X + c.LEFT * speed)
                    self.SetMoved(True)
        elif roll == 2:
            if not self._game.collide(my_id, True, self._X, self._Y + c.UP * speed):
                if self._game.legal_field(self._X, self._Y, 0, c.UP, speed):
                    self.Set_Y(self._Y + c.UP * speed)
                    self.SetMoved(True)
        elif roll == 3:
            if not self._game.collide(my_id, True, self._X + c.RIGHT * speed, self._Y):
                if self._game.legal_field(self._X, self._Y, c.RIGHT, 0, speed):
                    self.Set_X(self._X + c.RIGHT * speed)
                    self.SetMoved(True)
        elif roll == 4:
            if not self._game.collide(my_id, True, self._X, self._Y + c.DOWN * speed):
                if self._game.legal_field(self._X, self._Y, 0, c.DOWN, speed):
                    self.Set_Y(self._Y + c.DOWN * speed)
                    self.SetMoved(True)
        elif roll == 5 and self._game.is_hex():
            if not self._game.collide(my_id, True, self._X + c.LEFT * speed, self._Y + c.UP * speed):
                if self._game.legal_field(self._X, self._Y, c.LEFT, c.UP, speed):
                    self.Set_X(self._X + c.LEFT * speed)
                    self.Set_Y(self._Y + c.UP * speed)
                    self.SetMoved(True)
        elif roll == 6 and self._game.is_hex():
            if not self._game.collide(my_id, True, self._X + c.RIGHT * speed, self._Y + c.DOWN * speed):
                if self._game.legal_field(self._X, self._Y, c.RIGHT, c.DOWN, speed):
                    self.Set_X(self._X + c.RIGHT * speed)
                    self.Set_Y(self._Y + c.DOWN * speed)
                    self.SetMoved(True)

    def Action(self, id):
        self.Move(id, 1)

