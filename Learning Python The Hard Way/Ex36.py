from sys import exit # exit() used for exiting program
import random # used for randint() and shuffle()
from time import sleep # used for sleep()

def safe_path():
  """Function if player chooses the path without enemies"""
  print
  for x in range(0,5):
    print "'step'"
    sleep(.5)
  print
  print "Wow, that was quick.  You made it home without encountering any dangerous creatures!"
  print "Great job!\n"
  exit(0)

def dangerous_path():
  """Function if player chooses the path with enemies"""
  print
  for x in range(0,30):
    print "'step'"
    sleep(.5)
    if (random.randint(0,3) == 3):
      fight()
      print
  print "Congratulations, you made back home alive and kicking! Great job!"
  exit(0)

def no_path():
  """Function if player chooses path with no end"""
  print
  for x in range(0,random.randint(10,15)):
    print "'step'"
    sleep(.5)
  print
  dead("You wandered down the path, found no way out, got lost and died")

def fight():
  """Mini-game runs when player runs into a fight"""
  global health
  creature_health = random.randint(5,10) * 5

  print "\nFIGHT!!!"
  print "You just ran into a dangerous creature with %d points health." % creature_health

  choice = str(raw_input("Do you fight or run? "))

  if choice == "run":
    if (random.randint(0,1) == 0):
      print "\nWhew, you ran from the fight without getting hurt!"
      print "Your health: %d\n" % health
    else:
      print "\nThe creature injured you while you ran! 20 points damage!"
      health -= 20
      print "Your health: %d\n" % health

  elif choice == "fight":
    print "\nSomeone's fearless!"
    print "Your health is %d, don't lose too much.\n" % health

    while creature_health > 0:
      attack = str(raw_input("Do you punch, kick or ram the creature? "))
      if attack == "punch":
        print "You punched the creature and did 10 points damage!"
        creature_health -= 10
        print "Creature health: %d" % creature_health
        print "Your health: %d" % health

      elif attack == "kick":
        print "You kicked the creature and did 15 points damage!"
        creature_health -= 15
        print "Creature health: %d" % creature_health
        print "Your health: %d" % health

      elif attack == "ram":
        print "You rammed the creature and did 10 points damage!"
        print "In the process you also did 15 points damage to yourself as well!"
        print "Ouch"
        creature_health -= 10
        health -= 15
        print "Creature health: %d" % creature_health
        print "Your health: %d" % health

      else:
        print "The creature attacked you while you were thinking. 20 POINTS! OUCH!"
        health -= 30
        print "Your health: %d\n" % health

      if (creature_health <= 0):
        print "You defeated the creature, good job!"
        print "Your health: %d\n" % health
        break;

      else:
        if (random.randint(0,1) == 0):
          print "\nThe creature tried to attack you, but missed! You got lucky!"
        else:
          creature_attack = random.randint(1,10) * 5
          print "\nThe creature attacked you! You lost %d health points!" % creature_attack
          health -= creature_attack
          print "Your health: %d\n" % health

      if (health <= 0):
        dead("Darn, you died fighting the creature.  Atleast you fought well.")

  else:
    dead("The animal ate you while you were thinking what to do.")

  if (health <= 0):
    dead("Darn, you died fighting the creature.  Atleast you fought well.")

def dead(why):
  """Displays prompt and kills program if player dies"""
  print why
  exit(0)

def start():
  """Starts game and gathers initial data"""
  print "Welcome!"
  print "Before we start, let's find out who you are."

  start = False

  while not start:
    name = str(raw_input("What's your name? "))
    print "Is this correct? \"%s\"" % name
    check = str(raw_input("y/n? "))

    if check in ("y", "Y", "yes", "Yes"):
      print "\nGreat! Let's begin!"
      start = True
    elif check in ("n", "N", "no", "No"):
      print "\nOk, let's try that again."
    else:
      print "\nLet's try and answer the question correctly, ok?"

  print """
%s, your journey begins at a crossroads deep within a forest,
at a place you've never seen before\n
You can travel down one of three paths.
One to your left, one to your right, and one straight ahead.\n
You must get back home before dark,
as these woods contain many dangerous creatures.\n
What path will you choose?
""" % name

  global health
  health = 100

  func_list = [safe_path, dangerous_path, no_path]
  random.shuffle(func_list)

  path = str(raw_input("Left, Right or Straight? "))

  if path in ("left", "Left", "l", "L"):
    func_list[0]()
  elif path in ("right", "Right", "r", "R"):
    func_list[1]()
  elif path in ("straight", "Straight", "s", "S"):
    func_list[2]()
  else:
    dead("You ventered into unknown territory, got lost and died.")

start()