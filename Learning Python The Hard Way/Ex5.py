name = 'Joel A. Santiago'
age = 27
height = 70 # inches
weight = 180 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

# Inserting variables into strings
print "Let's talk about %s." % name
print "He's %d inches or %d centimeters tall." % (height, height * 2.54)
print "He's %d pounds or %d kilos heavy." % (weight, weight * 0.453592)
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the soda." % teeth

# Inserting multiple variables into a string
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)