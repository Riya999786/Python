__author__ = 'Joel Santiago'

from Player import Player
from Creature import Creature
from Map import Map


class Engine(object):

    def __init__(self):
        pass

    def checkDifficulty(self, x):
        dict_difficulty = {"Easy": 4, "Medium": 3, "Hard": 2}
        if x in dict_difficulty:
            return dict_difficulty[x]
        else:
            print "This difficulty isn't a valid option\n"
            return False

    def start(self):
        """Starts game and gathers initial data"""
        global name
        print "Welcome!"
        print "Before we start, let's find out who you are."

        while True:
            name = str(raw_input("What's your name? "))

            while True:
                difficulty = str(raw_input("What difficulty would you like to play with (Easy, Medium, Hard)? "))
                user_difficulty = self.checkDifficulty(difficulty)
                if user_difficulty:
                    break

            print "\nName: %s\nDifficulty: %s" % (name, difficulty)
            check = str(raw_input("Is this correct (yes/no)? "))

            if check in ("y", "Y", "yes", "Yes"):
                print "\nGreat! Let's begin!\n"
                break
            elif check in ("n", "N", "no", "No"):
                print "\nOk, let's try that again."
            else:
                print "\nLet's try and answer the question correctly, ok?"

        player = Player(name)
        game_map = Map(user_difficulty)

        print "You're presented with a grid of 10 rows and 10 columns."
        print "If you want to win, you need to make it through 10 steps within the grid."
        print "But be careful, the grid is littered with creatures waiting to attack."
        print "One wrong step and you could be dead."
        print "Enjoy."
        print

        self.steps = 10
        print "Where would you like to start?\n"
        while self.steps > 0:
            game_map.displayMap(game_map.blankList)
            print "Steps remaining: %d\n" % self.steps

            monster = Creature()
            try:
                row = int(raw_input("Row location (0-9): "))
                col = int(raw_input("Column location (0-9): "))
                self.steps -= 1
                player.navigate(row, col, game_map, monster)
                if player.health <= 50 and player.potions > 0:
                    p_choice = raw_input("Would you like to use a potion? (%d remaining) " % player.potions)
                    if p_choice in ("y", "Y", "yes", "Yes"):
                        player.potion()
                    elif p_choice in ("n", "N", "no", "No"):
                        print "Ok, just be careful"
                    else:
                        print "Hmm, guess you don't really need a potion!"
                print
            except ValueError:
                print "Enter a number 0-9\n"

        print "Congratulations! You made it through the map!"

game = Engine()
game.start()