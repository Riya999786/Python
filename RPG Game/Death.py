__author__ = 'Joel Santiago'

from random import randint


class Death(object):

    responses = [
        "Seriously? Try harder! (and again)",
        "I've seen babies do better than you!",
        "Just.........no, you just died",
        "Ok, you were kinda on the right track, then you weren't.  So sad."
    ]

    def died(self):
        print self.responses[randint(0, len(self.responses) - 1)]
        exit(0)
