__author__ = 'Joel Santiago'

from Death import Death
from random import randint


class Battle(object):
    def __init__(self, player, creature):
        self.player = player
        self.creature = creature

    def fight(self):
        dead = Death()

        print "\nFIGHT!!!"
        print "You just ran into %s with %d points health." % (self.creature.creature_name,
                                                               self.creature.creature_health)

        choice = str(raw_input("Do you fight or run? "))

        if choice in ["run", "Run"]:
            if randint(0, 1) == 0:
                print "\nWhew, you ran from the fight without getting hurt!"
                print "Your health: %d\n" % self.player.health
            else:
                print "\n%s injured you while you ran! 20 points damage!" % self.creature.creature_name
                self.player.health -= 20
                print "Your health: %d\n" % self.player.health

        elif choice in ["fight", "Fight"]:
            print "\nSomeones fearless!"
            print "Your health is %d, don't lose too much.\n" % self.player.health

            while self.creature.creature_health > 0:
                attack = str(raw_input("Do you punch, kick or ram %s? " % self.creature.creature_name))
                if attack in ["punch", "Punch"]:
                    print "You punched %s and did 10 points damage!" % self.creature.creature_name
                    self.creature.creature_health -= 10
                    print "Creature health: %d" % self.creature.creature_health
                    print "Your health: %d" % self.player.health

                elif attack in ["kick", "Kick"]:
                    print "You kicked %s and did 15 points damage!" % self.creature.creature_name
                    self.creature.creature_health -= 15
                    print "Creature health: %d" % self.creature.creature_health
                    print "Your health: %d" % self.player.health

                elif attack in ["ram", "Ram"]:
                    print "You rammed %s and did 15 points damage!" % self.creature.creature_name
                    print "In the process you also did 15 points damage to yourself as well! OUCH!"
                    self.creature.creature_health -= 15
                    self.player.health -= 15
                    print "Creature health: %d" % self.creature.creature_health
                    print "Your health: %d" % self.player.health

                else:
                    print "%s attacked you while you were thinking. 20 POINTS! OUCH!" % self.creature.creature_name
                    self.player.health -= 20
                    print "Your health: %d\n" % self.player.health

                if self.creature.creature_health <= 0:
                    print "You defeated %s, good job!" % self.creature.creature_name
                    print "Your health: %d\n" % self.player.health
                    break

                else:
                    if randint(0, 1) == 0:
                        print "\n%s tried to attack you, but missed! You got lucky!" % self.creature.creature_name
                    else:
                        creature_attack = randint(1, 10) * 5
                        print "\n%s attacked you! You lost %d health points!" % (self.creature.creature_name,
                                                                                 creature_attack)
                        self.player.health -= creature_attack
                        print "Your health: %d" % self.player.health

                if self.player.health <= 0:
                    dead.died()

        else:
            dead.died()

        if self.player.health <= 0:
            dead.died()