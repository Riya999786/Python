# Import argv functionality from sys library
from sys import argv
# Import exists method from os.path library, used for comparison
from os.path import exists

# Assign arguments to their respective variables
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# Opens and reads from selected file
indata = open(from_file).read()

# Figures the length of the file in bytes
print "The input file is %d bytes long" % len(indata)

# Checks to see if a file with the same name exists in curr directory
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("> ")

# Opens the existing 2nd file to write to or creates a new file if no file exists
out_file = open(to_file, "w")
# Writes content from file 1 to file 2
out_file.write(indata)

print "Alright, all done"

# Closes new file
out_file.close()
