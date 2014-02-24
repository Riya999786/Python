# Initial prompt for the user
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

# Gather user input
door = raw_input("> ")

# If user entered '1' for door
if door == "1":
  print "There's a giant bear here eating a cheese cake.  What do you do?"
  print "1. Take the cake."
  print "2. Scream at the bear."

  # Gather new input from user
  bear = raw_input("> ")

  # If user entered '1' for bear
  if bear == "1":
    print "The bear eats your face off.  Good job!"
  # If user entered '2' for bear
  elif bear == "2":
    print "The bear eats your legs off.  Good job!"
  # If user entered anything else for bear
  else:
    print "Well, doing %s is probably better.  Bear runs away." % bear

# If user entered '2' for door
elif door == "2":
  print "You stare inot the endless abyss at Cthulhu's retina."
  print "1. Blueberries."
  print "2. Yellow jacket clothespins."
  print "3. Understanding revolvers yelling melodies."

  # Gather user input
  insanity = raw_input("> ")

  # If user entered '1' or '2' for insanity
  if insanity == "1" or insanity == "2":
    print "Your body survives powered by a mind of jello.  Good job!"
  # If user entered anything else for insanity
  else:
    print "The insanity rots your eyes into a pool of muck.  Good job!"

# If user entered anything else for door
else:
  print "You stumble around and fall on a knife and die.  Good job!"