# For each of the above features you should do the following:
#   a.  Write a short program or programs to investigate its use.
#       You may combine more than one feature into a single program.
#   b.  Explain how the feature works in Python and compare it to one or more languages with which you are familiar.
#   c.  Critique the implementation or use of the feature or construct.

# 1. Interpretation
print "1. Interpretation"

## a. Implementation
print "\tNo example possible"

## b. Explanation / Comparison
"""
Python is a strictly interpreted language (like PHP) in that it doesn't need to be compiled in the same process as C needs to be
compiled.  However, it is compiled into byte code and is then executed in the Python VM.  Unlike Python, Java takes the
java files and compiles them into individual class files and then adds them together and runs the program.
"""

## c. Critique
"""
Being that Python is an interpreted language, it's useful for a plethora of functions.  I like that it's flexible enough
to be used on a client side computer or on the server side to be used as a web site backend.
"""

print

# 2. Boolean Expression
print "2. Boolean Expression"

## a. Implementation
print "\t(2 ** 2 == 4) = " + str(2 ** 2 == 4)
print "\t(1 < 0) = " + str(1 < 0)
print "\t(50 % 5 == 0) = " + str(50 % 5 == 0)

## b. Explanation / Comparison
"""
Boolean expressions in Python work very similar to languages like C or Java.  You can simply type any expression
and it will be evaluated to either True or False.  In some ways, the Python implementation is simpler than the same
in Java in that you can print out the entire expression within a print statement, and the readability is much easier.
In Java, you have to run through the entire System.out.println() and fit the expression within the println.
Surprisingly, the Python implementation is similar to the same in C.
"""

## c. Critique
"""
The use of Boolean Expressions in Python is surpisingly simple and very understandable and its results are very
clearly printed and obvious.  It's simply an equality check and aside from using non-traditional operators, I think
anyone could take a look at the expression and give an answer.
"""

print

# 3. Short Circuit Evaluation
print "3. Short Circuit Evaluation"

## a. Implementation
print "\tTrue and False = " + str(True and False)
print "\tTrue or False = " + str(True or False)

## b. Explanation / Comparison
"""
Pythons use of Short Circuit Evaluation is incredibly similar to many other languages, like C or Java.  It's simply
a use of and or (and nor and xor) and is just used to compare whether both variables are True for "and", or if just one
is True for "or".  Much like Boolean expression, the results are printed out incredibly clearly, enough for even
beginners to the language.
"""

## c. Critique
"""
Much like others languages, Short Circuit Evaluation is very simple to implement, in Python and in other languages.
You just use 'and' or 'or' and compare variables.  The only problem I see when implementing this type of check is that
you have to understand the logic.  While the wording is simple to read, the logic can be confusing for someone who's
not familiar with the use.  Aside from this small problem, the implementation is very simple to apply.
"""

print

# 4. Numeric Types
print "4. Numeric Types"

## a. Implementation
integer_val = 31
float_val = 5.5
print "\tInteger"
print "\t" + str(integer_val)
print "\t" + str(type(integer_val))
print
print "\tFloat"
print "\t" + str(float_val)
print "\t" + str(type(float_val))

## b. Explanation / Comparison
"""
Unlike many other languages, Python doesn't require the programmer to identify each variable with a type. Each variable
takes a look at the value that is assigned to it and designates the type based on said value.  Simply, the difference
between and 'int' and a 'float' is 5 and 5.0.  Languages like C and Java require each variable to identified by its
corresponding type, so python simplifies it quite a bit.  The type is also still retrievable by using the type() method above
and can be recast into other types by using the str() method shown above.
"""

## c. Critique
"""
Implementing types to variables in Python is incredibly simple and in my opinion, is a much better way of working with
variables.  Removing the type declaration makes the variable more flexible and clears up the code a little bit more as
well.  Other languages that require the type to be declared before the variable name now seem a little redundant, since
the value assigned to the variable denotes what type the variable is.
"""

print

# 5. Strings
print "5. Strings"

## a. Implementation
print "\tThis is a string literal example"
print "\tI'm just being printed out to the console using a print statement"

## b. Explanation / Comparison
"""
Much like the numeric type identifers, strings are similarly defined simply by naming a variable and writing out a
string.  Strings in Python are somewhat similar to those in Java in that you can declare a variable and simply write
out the string itself.  However, in C, you have to work with a char* to accomodate a string, which is much more
cumbersome.  One nice thing about strings in Python is that each letter has an index, much like an array, so it is
possible to get a specific letter if need be.
"""

## c. Critique
"""
Strings are incredibly easy to work with in Python.  All you have to do is declare the variable and write the string.
It's so much easier than working with strings in C which aren't exactly strings, moreso char*.  You don't even need to
declare a variable for the string; instead just printing it to console directly.  The downside to this is that if you
want to mix in any variables, you have to either cast it to a string using str() or using tokens to place them in the
string.
"""

print

# 6. Arrays
print "6. Arrays"

## a. Implementation
my_array = []
print "\tmy_array[] = x ** 3 for x in range(0,11)"
for x in range(0, 11):
    my_array.append(x ** 2)
print "\tmy_array[] = " + str(my_array)

## b. Explanation / Comparison
"""
Arrays in Python aren't always going to be implemented as array, depending on how many dimensions you're planning on
implementing.  If you're using a simple 1D array, then a list is ideal as it is similarly written like an array and can
hold multiple variables using an index.  A 2D array or higher can then either be implemented as a list or can be written
as an array type, though lists tend to be more than ideal in most instances.  Arrays tend to be most useful when using
data that is more C like (unsigned int,...), but mostly, lists will suffice.
"""

## c. Critique
"""
I find that if I'm ever in need of an array like structure, I find myself using lists as they are much easier to work
with and iterate through and work almost identically like an array.  Even implementing a 2D array is as simple as using
two for loops to iterate through both dimensions.  Lists in Python, in some instances, make arrays from other languages
look significantly more tiring to work with.
"""

print

# 7. Lists
print "7. Lists"

## a. Implementation
list_one = [x ** 3 for x in range(0, 50) if x % 3 == 0]
print "\tList_One = " + str(list_one)

## b. Explanation / Comparison
"""
Lists in Python seem much like arrays in C and in Java.  Declaring a list looks just lke creating an array with values
at various indexes.  One really nice thing about lists in python is that you don't initially need to define how large a
list will be.  You simply declare a blank list by using the [] operators by themselves.  Lists can also be two
dimensional and hold lists within themselves.
"""

## c. Critique
"""
As I mentioned before, the fact that you don't have to initially declare the list length is really nice if you aren't
certain about the size the list will grow to.  Another thing thats really nice about lists is exemplified above.  You
can use a for loop to auto-create the array, granted this only works for certain types.  Lists in Python, just seem
significantly easier to implement and use than arrays of other languages.
"""

print

# 8. Tuples
print "8. Tuples"

## a. Implementation
tuple_one = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print "\tTuple_One = " + str(tuple_one)

## b. Explanation / Comparison
"""
Tuples in Python are quite a bit like lists in Python.  They look much like lists, thus also look like arrays from C and
Java, but there is one significant difference.  Tuples are immutable, or uneditable, where as lists allow you to edit
them after their creation.  Lists and Tuples (and later, dictionaries), while initially similar looking, are
differentiated by their symbols.  Lists use [] brackets whereas Tuples use () brackets.
"""

## c. Critique
"""
Like lists, tuples are easy to implement and use as well.  They're beneficial for fixed lists of data, however, if you
are going to be editing the data in any way, it's better to use a list.  Tuples also have the added benefit of being
able to be auto-created by using the range() function or other methods.
"""

print

# 9. Slices
print "9. Slices"

## a. Implementation
slice_list = range(0, 31)
print "\tSlice_List = " + str(slice_list)
print "\tSlice_List[15:45:2] = " + str(slice_list[5:28:2])

## b. Explanation / Comparison
"""
Slices are a very simple way to quickly grab a range of values from a list in Python.  You have three values that can be
defined when creating the slice.  You have the starting point (inclusive), the ending point (exclusive), and the
stepping value that be positive or negative, denoting moving forward or backward through the slice values.  From the
example above, the slice takes the values between 5 and 27, stepping forward every other value, grabbing all the odd
values.  You don't even need to define all the values, instead you can just leave one value defined and the others
blank, which would end up looking like [::2].  This would step through the entire list from start to end, stepping up
every other value.  Aside from using a for loop in C or Java, I don't know of any other language that has similar
functionality.
"""

## c. Critique
"""
Slices are an incredibly easy way to grab a portion of information from any list.  It's highly customizable and is quick
to implement and is fairly obvious as to what function the code is performing.  As I mentioned earlier, I'm not aware of
any language that has as simple a method of getting a specific block of data from a list, which really gives the edge to
Python.
"""

print

# 10. Index Range Checking
print "10. Index Range Checking"

## a. Implementation
print "\tNo example possible"

## b. Explanation / Comparison
"""
Python uses runtime range checking to verify if the variables that are defined in the code are within the range of
whatever type they are declared as, to ensure the program runs correctly and that an exception isn't thrown.
"""

## c. Critique
"""
There isn't much that I can critique on the feature here as it's not one I encounter directly, however one side effect
of the checking being done at runtime is that errors don't usually show up until the program is told to run.  While this
allows the programmer to think that the code is correct, it could lead to many errors that pop up directly at run time,
preventing the code from functioning correctly.
"""

print

# 11. Dictionaries
print "11. Dictionaries"

## a. Implementation
dict_one = {"Joel": 1, "Mike": 2, "Sandra": 3, "James": 4, "Tom": 5}
print "\tDict_One = " + str(dict_one)
for key in dict_one:
    print "\t\tKey: " + str(key)
    print "\t\tValue: " + str(dict_one[key])
    print

## b. Explanation / Comparison
"""
Much like lists, Dictionaries look like lists or Tuples in that they store a variety of information in a list looking
design, but have one major difference.  Whereas lists have only the values at a predefined index value, each value in a
dictionary has it's own key and value.  So you are able to search the dictionary based on either the key or the value
for each value stored within the dictionary.  Dictionaries also have their own differentiating symbols, using {} instead
of [] like lists or () like tuples.  Unlike other languages like C, Python dictionaries allow you to not only set the
value, but the key as well.  Arrays in c only let you define the value, while the index is automatically incremented.
A two dimensional array could be used to replicate the functionality of a dictionary, however, it would get complicated
fast.
"""

## c. Critique
"""
Dictionaries are a really simple way to manage every piece of information that is stored.  It's a very clean to way to
store a data point to a specific value.  Not to mention, the layout of the contents of the dictionary are incredibly
easy to understand even for a non programmer.
"""

print

# 12. If Statement
print "12. If Statement"

## a. Implementation
test_val = 1
print "\tTest_Val = " + str(test_val)
print "\tEntering the if-elif-else statement, what prints?"
print
if 30 % 5 == test_val:
    print "\t\tChecking (30 % 5) == test_val"
    print "\t\tI'm in the if statement"
elif 25 % 8 == test_val:
    print "\t\tChecking 25 % 8 == test_val"
    print "\t\tI'm in the elif statement"
else:
    print "\t\tI'm in the else statement"

## b. Explanation / Comparison
"""
If statements are nearly identical to if statements in C or Java.  The main difference is that in Python, the 'else if'
statement has been shortened to 'elif' which makes plenty sense.  One other difference is that there is no need for
parenthesis to surround the code being check, instead you just type it out.  Also, as is the case for a majority of
functions in Python, after each statement, you begin the code block by using a colon : which acts like { bracket in C.
"""

## c. Critique
"""
Implementing an If statement in Python is incredibly easy, though not much different than other languages.  So there
isn't a huge improvement in Python versus other languages.  The only real benefit Python gives the programmer is that
you don't need to use parenthesis to surround the code, which makes the code seem cleaner to the reader.
"""

print

# 13. Switch Statement
print "13. Switch Statement"

## a. Implementation
print "\tThere currently are no switch or case statements within the Python language"
print "\tDocumentation suggest that programmers use If/Elif/Else statements instead"

## b. Explanation / Comparison
"""
There isn't much to explain since there is no current implementation of a switch statement in the Python language.  The
documentation even says that using an if-elif-else statement would be just as functional and is the recommended method.
"""

## c. Critique
"""
While I see the benefit to switch statements in letting you do a single check of a variable which then dictates what
functionality is chosen, this can also be easily implemented using a simple if else statement.  Aside from that, the
design of switch statements, to me, seem to go against the way python is structured and designed.
"""

print

# 14. For Loop
print "14. For Loop"

## a. Implementation
for_list = range(0,26)
print "\tFor_List = " + str(for_list)
for x in for_list:
    if x % 5 == 0:
        print "\t\tx in for_list = " + str(x)

## b. Explanation / Comparison
"""
For loops in Python are a much more simplified version of for loops when compared the likes in C or Java.  In C you need
to define the incrementer variable, the range the loop runs through and then that the value increments.  In Python, all
you need to do is define the value that stands for the value in the list you're looping through, and the list that you
will be looping through.  The loop auto-increments through the list after the code block is completed.  The for loop in
Python is actually quite similar to the foreach loop in PHP that also auto-increments through the array.
"""

## c. Critique
"""
This design of a for loop in Python is significantly easier than other languages.  The syntax is much cleaner and there
isn't a lot of defining thats needed, as the loop handles most of the work itself.  I wouldn't be against other
languages implementing loops like this, though I'm already plenty comfortable with how the loops are structured in other
languages.  This way just seems easier.
"""

print

# 15. While Loop
print "15. While Loop"

## a. Implementation
i = 0
print "\twhile i <= 10:"
while i <= 10:
    print "\t\ti = %s" % i
    i += 1

## b. Explanation / Comparison
"""
The while loop in Python is almost identical to the while loop in C and Java as it's nothing more than stating the
expression being tested after the 'while' identifier.  Nothing fancy like auto incrementing is done, it's just a simple
check of an expression, followed by a colon designating where the code block begins.  The while loop in C is almost 100%
identical to the Python equivalent, so there really isn't much to compare.
"""

## c. Critique
"""
As i mentioned above, the while loop in Python is as simple as the while loop in other languages, much because it is
nearly identical to the implementation in other languages.  So due the already simplistic nature of the while loop, it's
easy to implement here.  The only difference i can say is that, like the if statement, no parenthesis are needed around
the expression being tested.  This again aids in legibility and cleanliness throughout the code, which is always a good
thing.
"""

print

# 16. Indentation to Denote Code Blocks
print "16. Indentation to Denote Code Blocks"

## a. Implementation
def print_function_indentation():
    print "\t\tprint_function_indentation()"
    print "\t\t\tThis is a print string within print_function_indentation()"
    print "\t\t\tThere are no { } brackets, instead a tab or 4 spaces denotes a code block"

print "\tcalling print_function_indentation()"
print_function_indentation()

## b. Explanation / Comparison
"""
Not much needs to be said about this due to its very simple nature, but whitespace is very important in Python.  Unlike
C and Java where functions and code blocks are denoted by { } brackets, allowing the code to be placed anywhere within
and at any tab stop, Python requires a tab or 4 spaces to denote the block of code.  The code needs to look structured
so that the code block is recognized, whereas other languages don't need this but use it still to aid in understanding
where certain code begins and ends.
"""

## c. Critique
"""
The lack of brackets initially felt a little odd, but really it allows for much cleaner looking code. Despte this being
a somewhat small feature, it ends up being a very useful addition due to how it benefits the programmer in reading the
code.  To me atleast, it makes the code read better and just simply looks better on the page.  In my opinion, this would
be a great improvement to other languages.
"""

print

# 17. Type Binding
print "17. Type Binding"

## a. Implementation
print "\tThere is no type binding within Python.  You simply declare a variable"
print "\twith a value and it is automatically assigned a type 'behind the scenes.'"
print "\t\tEXAMPLE: my_integer = 15 would be cast as an int without needing the 'int' text"
print "\t\tEXAMPLE: my_string = \"this is an example string\" is cast as a string without needing the 'string' text"

## b. Explanation / Comparison
"""
Languages like C and java require the programmer to specificy what type the variable being defined will actually be. So
an int would be designated an int by the programmer.  In Python however, variables don't need a type designation, as the
variable checks what value has been assigned to it and designated the type to the variable.  This really cleans the code
up.
"""

## c. Critique
"""
I really like this feature of python as it's just a simpler way to approach the definition of new variables.  Having an
int be designated an int and assigning an int to it seems a little too redundant to me, and Python makes it a point to
fix this redundancy.  The variable still has a designated type, it's just not written out, and the variable can still be
cast to other types, but this methodology of not writing out the type just seems to be a better way of programming.
"""

print

# 18. Type Checking
print "18. Type Checking"

## a. Implementation
new_string = "This is a testing string"
print "\tnew_string = " + new_string
print "\t\tisinstance(new_string, str) = " + str(isinstance(new_string, str))
print
new_int = 8675309
print "\tnew_int = " + str(new_int)
print "\t\tisinstance(new_int, int) = " + str(isinstance(new_int, int))

## b. Explanation / Comparison
"""
Type checking in Python isn't something that typically needs to be done as it's a fairly dynamic language and doesn't
force static type checking at compile time.  This allows for more flexibility and adaptability to whatever code you
write, whereas other languages that require static checking limit what you can perform as well as how much code needs to
be written.  However, you can still use certain Python functions to actually check the type and return True or False, as
exemplified above.
"""

## c. Critique
"""
While a lot of the functionality of being dynamically typed happens behind the scene, the aspect that the programmer
will encounter all the time will be the amount of code that can be cut out due to this feature.  It takes a long line
and reduces it to something significantly smaller.  One other thing I've encountered is that with function accepting
parameters, they aren't tied down to a type of parameter, instead can recieve a plethora of parameters due to the lack
of type checking.
"""

print

# 19. Functions
print "19. Functions"

## a. Implementation
print "\tFunction average_of_num(num) is called to calculate average of arguments"
def average_of_num(num):
    sum_of_num = sum(num)
    average = sum_of_num / len(num)
    return average

avg_list = range(0, 10)
print "\t\tavg_list[] = " + str(avg_list)
print "\t\tAverage_of_Num(avg_list) = " + str(average_of_num(avg_list))

## b. Explanation / Comparison
"""
Functions in Python much like other variables are much simpler to write out and due to the lack of type checking, are
significantly more dynamic in nature, than the likes in C or Java.  You write out def which signifies a function will be
created, then assign the function name and list any parameters within parenthesis.  In c, the function type determines
what kind of value will be returned, whereas in Python, any value can be returned assuming it hasn't been cast as a
different type.
"""

## c. Critique
"""
Looking at the example above, no type is specified so the function can recieve any type and return any type.  Also note
that no other brackets are needed to denote the code block which makes the code look much cleaner.  calling the function
looks much like C and Java but this implementation is just much easier to work with, and if coded correctly, can be
reused in several places for several types of variables.
"""

print

# 20. Enumerate
print "20. Enumerate"

## a. Implementation
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print "\ta[] = " + str(a)
for index, item in enumerate(a):
    print "\t\tindex: " + str(index) + " key: " + str(item)

## b. Explanation / Comparison
"""
The enumerate function is a great way of retreiving data from lists, but instead of only returning the value from the
lists, the programmer gets back the value and the index of the value as well.  From the best of my knowledge, I don't
know of any way to easily get the index and value from an array in C aside from setting up a for loop and assigning each
value to a variable.  Thinking about it, this method is somewhat similar to the enumerate() function in Python, but here
we have a simple function to do this for us.
"""

## c. Critique
"""
After thinking about it above, the function of the enumerate() method is to retrieve an index and value from a list.
Doing the same thing in C is not significantly more difficult but can obviously be simplified which it has been in the
Python language.  In the example above, I still used a for loop, but it contained much less code due to the enumerate
function.  Either way, this method is still a great way to get all the information about a variable in a list in an easy
manner.
"""


#Output from Program
"""
1. Interpretation
	No example possible

2. Boolean Expression
	(2 ** 2 == 4) = True
	(1 < 0) = False
	(50 % 5 == 0) = True

3. Short Circuit Evaluation
	True and False = False
	True or False = True

4. Numeric Types
	Integer
	31
	<type 'int'>

	Float
	5.5
	<type 'float'>

5. Strings
	This is a string literal example
	I'm just being printed out to the console using a print statement

6. Arrays
	my_array[] = x ** 3 for x in range(0,11)
	my_array[] = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

7. Lists
	List_One = [0, 27, 216, 729, 1728, 3375, 5832, 9261, 13824, 19683, 27000, 35937, 46656, 59319, 74088, 91125, 110592]

8. Tuples
	Tuple_One = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

9. Slices
	Slice_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
	Slice_List[15:45:2] = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]

10. Index Range Checking
	No example possible

11. Dictionaries
	Dict_One = {'James': 4, 'Joel': 1, 'Tom': 5, 'Mike': 2, 'Sandra': 3}
		Key: James
		Value: 4

		Key: Joel
		Value: 1

		Key: Tom
		Value: 5

		Key: Mike
		Value: 2

		Key: Sandra
		Value: 3


12. If Statement
	Test_Val = 1
	Entering the if-elif-else statement, what prints?

		Checking 25 % 8 == test_val
		I'm in the elif statement

13. Switch Statement
	There currently are no switch or case statements within the Python language
	Documentation suggest that programmers use If/Elif/Else statements instead

14. For Loop
	For_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
		x in for_list = 0
		x in for_list = 5
		x in for_list = 10
		x in for_list = 15
		x in for_list = 20
		x in for_list = 25

15. While Loop
	while i <= 10:
		i = 0
		i = 1
		i = 2
		i = 3
		i = 4
		i = 5
		i = 6
		i = 7
		i = 8
		i = 9
		i = 10

16. Indentation to Denote Code Blocks
	calling print_function_indentation()
		print_function_indentation()
			This is a print string within print_function_indentation()
			There are no { } brackets, instead a tab or 4 spaces denotes a code block

17. Type Binding
	There is no type binding within Python.  You simply declare a variable
	with a value and it is automatically assigned a type 'behind the scenes.'
		EXAMPLE: my_integer = 15 would be cast as an int without needing the 'int' text
		EXAMPLE: my_string = "this is an example string" is cast as a string without needing the 'string' text

18. Type Checking
	new_string = This is a testing string
		isinstance(new_string, str) = True

	new_int = 8675309
		isinstance(new_int, int) = True

19. Functions
	Function average_of_num(num) is called to calculate average of arguments
		avg_list[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		Average_of_Num(avg_list) = 4

20. Enumerate
	a[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
		index: 0 key: a
		index: 1 key: b
		index: 2 key: c
		index: 3 key: d
		index: 4 key: e
		index: 5 key: f
		index: 6 key: g
"""
