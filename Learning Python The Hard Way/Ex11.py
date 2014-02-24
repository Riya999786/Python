# Question and answer using raw_input to gather entered data
print "How old are you?"
age = raw_input()
print "Male or Female?"
sex = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

# Print out gathered data
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)