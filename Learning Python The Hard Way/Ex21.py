# 'add' function adds 2 arguments
def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b

# 'subtract' function subtracts 2 arguments
def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b

# 'multiply' function multiplies 2 arguments
def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b

# 'divide' function divides 2 arguments
def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b

print "Let's do some math with just functions!"

# Variable assignments
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"