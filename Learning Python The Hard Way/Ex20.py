# Import argv functionality from sys library
from sys import argv

# Unpack arguments from argv into their respective variables
script, input_file = argv

# 'print_all' function reads file
def print_all(f):
  print f.read()

# 'rewind' function returns file pointer back to start of file
def rewind(f):
  f.seek(0)

# 'print_a_line' function prints
def print_a_line(line_count, f):
  print line_count, f.readline(),

# Opens selected file
current_file = open(input_file)

print "First let's print the whole file:\n"

# 'print_all' function call with file as argument
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# 'rewind' function call with file as argument
rewind(current_file)

print "Let's print three lines:"

# Function calls each printing the next line
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)