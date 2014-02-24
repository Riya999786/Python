# Ex 37: Symbol Review

# KEYWORDS
print "KEYWORDS"

# and
print "1. and"
print True and False
print

# del
print "2. del"
list = [1, 2, 3, 4, 5]
print "list =", list
del(list[2])
print "del(list[2])"
print "list =", list
print

# from
print "3. from"
from random import shuffle
list = [1, 2, 3, 4, 5]
print "list =", list
shuffle(list)
print "shuffle(list)"
print "list =", list
print

# not
print "4. not"
choice = True
print "choice = %s" % str(choice)
print "not choice = %s" % str(not choice)
print

# while
print "5. while"
i = 1
while i <= 5:
  print "i = %d" % i
  i += 1
print

# as
print "6. as"
with open("test.txt", "r") as f:
  line = f.read()
  print line
print

# elif
print "7. elif"
test = False
if test:
  print "in the if statement"
elif not test:
  print "in the elif statement"
else:
  print "in the else statement"
print

# global
print "8. global"
num = 5
print "num before func = %d" % num
def func():
  global num
  num = 42
func()
print "num after func = %d" % num
print

# or
print "9. or"
print True or False
print

# with
print "10. as"
with open("test.txt", "r") as f:
  line = f.readline()
  print line
print

# assert
print "11. assert"
d = '2011-02-07'
print "d = %s" % d
try:
  assert str(d) == '2011-02-07'
  print "assert str(d) equates True"
except:
  print "assert str(d) equates False"
print

# else
print "12. else"
test = False
if test:
  print "in the if statement"
elif not test:
  print "in the elif statement"
else:
  print "in the else statement"
print

# if
print "13. if"
test = False
if test:
  print "in the if statement"
elif not test:
  print "in the elif statement"
else:
  print "in the else statement"
print

# pass
print "14. pass"
def a():
  pass
print "Calling function a() with only pass statement"
a()
print "Called function a() resulting in a temporarily passed function"
print

# yield
print "15. yield"
def createGenerator(num):
  mylist = range(num)
  for i in mylist:
    yield i * i
print "Call createGenerator() with num = 4 and assign it to myGenerator"
myGenerator = createGenerator(4)
print "Iterate through myGenerator"
for i in myGenerator:
  print i
print

# break
print "16. break"
from random import randint
num = randint(0,10)
i = 0
test = True
while test:
  print i
  i += 1
  if i == num:
    test = False
    break
print

# except
print "17. except"
try:
  print 5 / 0
  print "Zero Division worked"
except ZeroDivisionError:
  print "Zero division did not work"
print

# import
import hashlib
print "18. import"
hash_object = hashlib.sha256(b'Password')
hex_dig = hash_object.hexdigest()
print "Password hashed using sha256: %s" % hex_dig
print

# print
print "19. print"
print "I'm using the print statement to print out this message!"
print

# class
print "20. class"
class Student:
  name = ""
  age = 0
  major = ""

  # The class "constructor" - It's actually an initializer
  def __init__(self, name, age, major):
      self.name = name
      self.age = age
      self.major = major

  def returnName(self):
    return self.name
  def returnAge(self):
    return self.age
  def returnMajor(self):
    return self.major

x = Student("Joel", 27, "Computer Science")
print x.returnName() + " " + str(x.returnAge()) + " " + x.returnMajor()
print

# exec
print "21. exec"
codeObject = compile("""
print "Hello, world"
""", '<string>', 'exec')
print "Executing codeObject"
exec codeObject
print

# in
print "22. in"
for x in range(0,10):
  print "x = %d" % x
print

# raise
print "23. raise"
choice = raw_input("Raise exception or not? yes/no: ")
if choice == "yes":
  raise NameError("Hi there")
elif choice == "no":
  print "Exception not raised"
else:
  print "wrong choice, try again"
print

# continue
print "24. continue"
for num in range(2, 10):
  if num % 2 == 0:
    print "Found an even number", num
    continue # continues the loop
  print "Found a number", num
print

# finally
print "25. finally"
try: # Will run if the code within can run
  print "I'm in the try block"
except: # If the try block fails, this block runs
  print "Now i'm in the except block"
finally: # This runs every time after either the try or except block
  print "Now i'm in the finally block"
print

# is
print "26. is"
x = []
print "x = []"
y = x
print "y = x"
print "x is y =", (x is y)
print

# return
print "27. return"
def func():
  return "I'm being returned from func()"
print func()
print

# def
print "28. def"
def func():
  return "This function was defined using 'def'"
print func()
print

# for
print "29. for"
print "The following range was printed using a 'for' loop"
for x in range(5,50,5):
  print x
print

# lambda
print "30. lambda"
def transform(n):
  print "transform returns x + %d" % n
  return lambda x: x + n
x = transform(5)
print "x(5) = %d" % x(5)
print

# try
print "31. try"
try: # Will run if the code within can run
  print "I'm in the try block"
except: # If the try block fails, this block runs
  print "Now i'm in the except block"
print

# DATA TYPES
print "DATA TYPES"

# True
print "1. True"
print "1 > 0:", 1 > 0
print

# False
print "2. False"
print "1 < 0:", 1 < 0
print

# None
print "3. None"
def func():
  pass
print "calling func returns:", func()
print

# strings
print "4. Strings"
print "This", "string", "was", "concatenated", "together", "plus", "the", "number", str(5), "which", "was", "an", "int", "before."
print

# numbers
print "5. numbers"
print

# floats
print "6. floats"
print "15.0 / 4 = %f" % (15.0 / 4)
print

# lists
print "7. lists"
myList = ["one", "two", "three", "four", "five"]
print "myList:", myList
del(myList[4])
print "del(myList[4])"
print "myList:", myList
print

# STRING ESCAPE SEQUENCES
print "STRING ESCAPE SEQUENCES"

# \\
print "1. \\Test string"
# \'
print "2. \'Test string"
# \"
print "3. \"Test string"
# \a
print "4. \aTest string"
# \b
print "5. \bTest string"
# \f
print "6. \fTest string"
# \n
print "7. \nTest string"
# \r
print "8. \rTest string"
# \t
print "9. \tTest string"
# \v
print "10. \vTest string"
print

# STRING FORMATS
print "STRING FORMATS"

# %d
print "1. %d" % 5
# %i
print "2. %i" % 5
# %o
print "3. %o" % 17
# %u
print "4. %u" % 20
# %x
print "5. %x" % 19
# %X
print "6. %X" % 18
# %e
print "7. %e" % (15.0/4)
# %E
print "8. %E" % (15.0/4)
# %f
print "9. %f" % (15.0/4)
# %F
print "10. %F" % (15.0/4)
# %g
print "11. %g" % (15.0/4)
# %G
print "12. %G" % (15.0/4)
# %c
print "13. %c" % 'c'
# %r
print "14. %r" % "string"
# %s
print "15. %s" % "string"
# %%
print "16. %%"
print

# OPERATORS
print "OPERATORS"

# +
print "1. 10 + 5 = %d" % (10 + 5)
# -
print "2. 5 - 10 = %d" % (5 - 10)
# *
print "3. 5 * 10 = %d" % (5 * 10)
# **
print "4. 2 ** 2 = %d" % (2 ** 2)
# /
print "5. 10 / 5 = %d" % (10 / 5)
# //
print "6. 9 // 2 = %d" % (9 // 2)
# %
# print "7. 10 % 3 = %d" % (10 % 3)
# <
print "8. 1 < 3 =", (1 < 3)
# >
print "9. 3 > 1 =", (3 > 1)
# <=
print "10. 5 <= 6 =", (5 <= 6)
# >=
print "11. 5 >= 5 =", (5 >= 5)
# ==
print "12. 10 == 8 =", (10 == 8)
# !=
print "13. True != False =", (True != False)
# <>
print "14. True <> False =", (True <> False)
# ( )
print "15. (1 + 2) * 3 = %d" % ((1 + 2) * 3)
# [ ]
myList = [1,2,3,4,5]
print "16.", myList
# { }
myDict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
print "17.", myDict
# @
print "18. "
# ,
print "19. "
# :
print "20. "
# .
print "21. "
# =
print "22. "
# ;
print "23. "
# +=
num = 1
num += 1
print "24. 1 += 1 = %d" % num
# -=
num = 1
num -= 1
print "25. 1 -= 1 = %d" % num
# *=
num = 2
num *= 2
print "26. 2 *= 2 = %d" % num
# /=
num = 10
num /= 2
print "27. 10 /= 2 = %d" % num
# //=
num = 10
num //= 4
print "28. 10 //= 4 = %d" % num
# %=
num = 10
num %= 4
print "29. 10 %= 4 =", num
# **=
num = 2
num **= 3
print "30. 2 **= 3 = %d" % num