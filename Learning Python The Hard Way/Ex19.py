# Define 'cheese_and_crackers' function with 2 args
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_crackers
  print "Man that's enough for a party!"
  print "Get a blanket.\n"

# Function call with defined arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Redefine variables to be passed to our function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Function call with newly defined arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Functino call with new arguments
print "we can even do the math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Function call with modified arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

var1 = int(raw_input("Value for var1: "))
var2 = int(raw_input("Value for var2: "))
cheese_and_crackers(var1, var2)