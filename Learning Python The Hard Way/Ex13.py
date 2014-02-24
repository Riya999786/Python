# Imports argv functionality from sys library
from sys import argv

# Assigns values from argv to their respective variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Get personal values using the specified prompts and raw_input
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So %s, you're %s years old, %s tall and weigh %s." % (first, age, height, weight)
