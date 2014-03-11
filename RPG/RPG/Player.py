__author__ = 'Joel Santiago'

from Battle import Battle
from random import randint


class Player(object):

    def __init__(self, name, potions):
        self.name = name
        self.health = 100
        self.potions = potions

    def navigate(self, x, y, Map, Monster):
        self.row = x
        self.col = y
        if Map.list[self.row][self.col] == 1:
            print "You found a Monster!"
            fight = Battle(self, Monster)
            Map.blankList[self.row][self.col] = "x"
            fight.fight()
        else:
            print "You found a safe spot!"
            Map.blankList[self.row][self.col] = "o"

    def potion(self):
        if self.potions == 0:
            print "You don't have anymore potions left! BE CAREFUL!"
            return
        else:
            self.potion_health = randint(3, 10) * 5
            self.health += self.potion_health
            print "You used a potion and restored %d points back to your health!" % self.potion_health
            self.potions -= 1
