# Imports ability to use command line arguments
from sys import argv

# Assigns arguments from command line to local variables
script, filename = argv

# Opens file with filename from command line argument
txt = open(filename)

print "Here's your file %r:" % filename
# Reads and closes file
print txt.read()
txt.close()