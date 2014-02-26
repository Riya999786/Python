__author__ = 'Joel Santiago'

from random import randint, choice


class Creature(object):

    # Based off of monsters from the film 'Cabin in the Woods'
    names = [
        "The Werewolf",
        "Clowns",
        "The Merman",
        "The Sugarplum Fairy",
        "Kevin",
        "An Angry Molesting Tree",
        "The Scarecrow Folk",
        "The Zombie Redneck Torture Family",
        "Deadites",
        "Sasquatch"
    ]

    def __init__(self):
        self.creature_name = choice(self.names)
        self.creature_health = randint(5, 10) * 5
