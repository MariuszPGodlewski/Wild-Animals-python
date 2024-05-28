from game.Animal import Animal

class Wolf(Animal):
    def __init__(self, game, position_X, position_Y, age=1):
        super().__init__(game, 9, 5, age, position_X, position_Y, "W")

    def baby(self, x, y):
        baby = Wolf(self._game, x, y)
        self._game.add_organism(baby)
        baby.set_moved(True)
        self._moved = True