# conditional excution:

# In order to write useful programs, we almost always need the ability to check 
# conditions
# and change the behavior of the program accordingly. 
# Conditional statements give us this
# ability. The simplest form is the if statement:
if x >  0:
    print('x is postitive')

# alternative execution:
# A second form of the if statement is “alternative execution”, in which 
# there are two possibilities
# and the condition determines which one runs. The syntax looks like this:
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

#chained conditionals:
# Sometimes there are more than two possibilities and we need more than two branches.
# One way to express a computation like that is a chained conditional:

if x < y:
    print ('x is less than y')

elif x > y:
    print('x is greater than y')
else:
    print ('x and y is equal')

# nested conditionals
# One conditional can also be nested within another. We could have written 
# the example in
# the previous section like this:

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

# The outer conditional contains two branches. The first branch contains a 
# simple statement.
# The second branch contains another if statement, which has two branches of its own.
# Those two branches are both simple statements, although they could have been 
# conditional
# statements as well.
# Although the indentation of the statements makes the structure apparent, 
# nested conditionals
# become difficult to read very quickly. It is a good idea to avoid them when you
# can.
# Logical operators often provide a way to simplify nested conditional statements. 
# For example,
# we can rewrite the following code using a single conditional:
# if 0 < x:
# if x < 10:
# print('x is a positive single-digit number.')
# The print statement runs only if we make it past both conditionals, 
# so we can get the same
# effect with the and operator:
# if 0 < x and x < 10:
# print('x is a positive single-digit number.')
# For this kind of condition, Python provides a more concise option:
# if 0 < x < 10:
# print('x is a positive single-digit number.')

# Recursion
# It is legal for one function to call another; it is also legal for a 
# function to call itself. It may
# not be obvious why that is a good thing, but it turns out to be one of 
# the most magical
# things a program can do. For example, look at the following function:
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
countdown(n-1)
# If n is 0 or negative, it outputs the word, “Blastoff!” Otherwise, 
# it outputs n and then calls
# a function named countdown—itself—passing n-1 as an argument.
# What happens if we call this function like this?
countdown(3)
# The execution of countdown begins with n=3, and since n is greater than 0, 
# it outputs the
# value 3, and then calls itself...
# The execution of countdown begins with n=2, and since n is greater than 0, it
# outputs the value 2, and then calls itself...
# The execution of countdown begins with n=1, and since n is greater
# than 0, it outputs the value 1, and then calls itself...
# The execution of countdown begins with n=0, and since n is
# not greater than 0, it outputs the word, “Blastoff!” and then
# returns.
# The countdown that got n=1 returns.
# The countdown that got n=2 returns.
# The countdown that got n=3 returns.
# And then you’re back in __main__. So, the total output looks like this:
3
2
1
Blastoff!
# A function that calls itself is recursive; the process of executing it is 
# called recursion.
# As another example, we can write a function that prints a string n times.
def print_n(s, n):
    if n <= 0:
        return
        print(s)
        print_n(s, n-1)

# Incremental development
# As you write larger functions, you might find yourself spending more time debugging.
# To deal with increasingly complex programs, you might want to try a process 
# called incremental
# development. The goal of incremental development is to avoid long debugging
# sessions by adding and testing only a small amount of code at a time.
# As an example, suppose you want to find the distance between two points, given 
# by the
# coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is:
# distance = (x2 - x1)2 + (y2 - y1)2
# The first step is to consider what a distance function should look like in Python. 
# In other
# words, what are the inputs (parameters) and what is the output (return value)?
# In this case, the inputs are two points, which you can represent using four numbers. 
# The
# return value is the distance represented by a floating-point value.
# Immediately you can write an outline of the function:
def distance(x1, y1, x2, y2):
return 0.0

# Obviously, this version doesn’t compute distances; it always returns zero. 
# But it is syntactically
# correct, and it runs, which means that you can test it before you make it more
# complicated.
# To test the new function, call it with sample arguments:
>>> distance(1, 2, 4, 6)
0.0
# I chose these values so that the horizontal distance is 3 and the vertical 
# distance is 4; that
# way, the result is 5, the hypotenuse of a 3-4-5 triangle. When testing a function, 
# it is useful
# to know the right answer.
# At this point we have confirmed that the function is syntactically correct, 
# and we can start
# adding code to the body. A reasonable next step is to find the differences 
# x2 􀀀 x1 and
# y2 􀀀 y1. The next version stores those values in temporary variables and prints them.
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
print('dx is', dx)
print('dy is', dy)
return 0.0
# If the function is working,it should display dx is 3 and dy is 4. 
# If so, we know that the
# function is getting the right arguments and performing the first 
# computation correctly. If
# not, there are only a few lines to check.
# Next we compute the sum of squares of dx and dy:
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
print('dsquared is: ', dsquared)
return 0.0
# Again, you would run the program at this stage and check the output (which should be
# 25). Finally, you can use math.sqrt to compute and return the result:
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
result = math.sqrt(dsquared)
return result
# If that works correctly, you are done. Otherwise, you might want to print the value of
# result before the return statement.
# The final version of the function doesn’t display anything when it runs; it only returns
# a value. The print statements we wrote are useful for debugging, but once you get the
# function working, you should remove them. Code like that is called scaffolding because it
# is helpful for building the program but is not part of the final product.
# When you start out, you should add only a line or two of code at a time. 
# As you gain more
# experience, you might find yourself writing and debugging bigger chunks. 
# Either way,
# incremental development can save you a lot of debugging time.
# The key aspects of the process are:
# 1. Start with a working program and make small incremental changes. At any point, if
# there is an error, you should have a good idea where it is.
# 2. Use variables to hold intermediate values so you can display and check them.
# 3. Once the program is working, you might want to remove some of the scaffolding or
# consolidate multiple statements into compound expressions, but only if it does not
# make the program difficult to read.
# As an exercise, use incremental development to write a function called 
# hypotenuse that
# returns the length of the hypotenuse of a right triangle given the lengths 
# of the other two
# legs as arguments. Record each stage of the development process as you go.