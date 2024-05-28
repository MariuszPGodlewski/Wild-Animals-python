from const import constants as c
from abc import ABC, abstractmethod


class Organism(ABC):
    def __init__(self, game, strength, initiative, age, position_X, position_Y, symbol, animal):
        self._game = game
        self._strength = strength
        self._initiative = initiative
        self._age = age
        self._X = position_X
        self._Y = position_Y
        self._symbol = symbol
        self._moved = False
        self._animal = animal

    @abstractmethod
    def baby(self, x, y):
        pass
    @abstractmethod
    def collidion(self, my_id, defender_id):
        pass
    @abstractmethod
    def Action(self, id):
        pass
    def SetMoved(self, moved):
        self._moved = moved

    def IncreaseAge(self):
        self._age += 1

    def GetStrength(self):
        return self._strength

    def StrengthAdjustment(self, bonus):
        self._strength += bonus

    def GetInitiative(self):
        return self._initiative

    def SetInitiative(self, initiative):
        self._initiative = initiative

    def GetAge(self):
        return self._age

    def AgeIncresse(self):
        self._age += 1

    def Get_X(self):
        return self._X

    def Set_X(self, position_X):
        self._X = position_X

    def Get_Y(self):
        return self._Y

    def Set_Y(self, position_Y):
        self._Y = position_Y

    def GetSymbol(self):
        return self._symbol

    def GetMoved(self):
        return self._moved

    def SetMoved(self, moved):
        self._moved = moved

    def IsAnimal(self):
        return self._animal
