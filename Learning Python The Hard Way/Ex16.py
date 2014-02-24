# Import argv functionality from the sys library
from sys import argv

# Assigns arguments from argv to their respective variables
script, filename = argv

# Give user choice to erase file or not
print "We're going to erase %r." % filename
print "If you don't want that, hid CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Prompt
raw_input("?")

# Opens file
print "Opening the file..."
target = open(filename, "r+")

# Display contents of the file
print "Contents to be erased from %r:" % filename
print target.read()
# Move file pointer back to the beginning
target.seek(0)

# Erase file to be made ready for new content
print "Truncating the file. Goodbye"
target.truncate()

print "Now I'm going to ask you for three lines."

# Gathers new text from user to written to file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file.\n"
string_format = "%s\n%s\n%s\n" % (line1, line2, line3)

# Writes new content to file
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(string_format)

# Display new contents of the file
print "New contents to be erased from %r:" % filename
# Move file pointer back to the beginning and print new contents
target.seek(0)
print target.read()

# Closes the file
print "And finally, we close it."
target.close()