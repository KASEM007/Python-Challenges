# Exercise 6.4
# A number, a, is a power of b if it is divisible
# by b and a/b is a power of b. Write a
# function called is_power that takes parameters a and b and returns 
# True if a is a 
# power of b. Note:
# you will have to think about the base case.

# def is_power(a,b):
#     if (a % b == 0):
#         return True
#         if (a/b == 1):
#             return True
#         else:
#             (is_power (a/b, b))
#     else:
#         return False

def is_power(a, b):
    # if a > 1 or b > 1:
    #     return ('Sorry, not a valid input')
    # elif a == 1 or  b == 1:
    #     return (1)
    # else:
    #     if a < 1 and b < 1:
    #         is_divisible(a,b)
    if is_divisible(a, b) == True: # calling the is_divisable function
        return (a, b) # if it return True that mean a is divisible by b
        if a/b == 1:
            return (a, b)
        else:
            is_power(a/b, b) # calling the is_power function
    else:
        return False


def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False




print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))


############################## Better Answer ###############################



TESTS

INPUT 10 2
OUTPUT False
COMMENT

10 is not power of 2.

INPUT 27 3
OUTPUT True
COMMENT

27 is power of 3 (3^3=27).

INPUT 1 1
OUTPUT True
COMMENT

1 is power of 1 (1^1=1).

INPUT 10 1
OUTPUT False
COMMENT

10 is not power of 1.

INPUT 3 3
OUTPUT True
COMMENT

3 is power of 3 (3^1=3).
"""

def is_divisible(a,b):
    """
        procedure is_divisible

        check if a is divisible by b (if so a should be multiple of b)

        parameters

        a(integer) first number (could be multiple of b)
        b(integer) second number (could be divisor of a)

        returns

        check(boolean) true if a is divisible by b, false in other case
    """
if a%b == 0:
        return True
    else:
        return False

def is_power(a,b):
# """
        # procedure is_power

        # check if a is power of b

        # condition, a is power of b if a is divisible by b and (a/b) is power of b

        # parameters

        # a(integer) first number (could be multiple of b)
        # b(integer) second number (could be divisor of a)

        # returns

        # check(boolean) true if a is power of b, false in other case
# """
    if a == b:
        return True
    elif b == 1:
        return False
    else:
        return is_divisible(a,b) and is_power(a/b,b)

if __name__=="__main__":
    print("is_power({0},{1}) returns: {2} ".format(10,2,is_power(10,2)))
    print("is_power({0},{1}) returns: {2} ".format(27,3,is_power(27,3)))
    print("is_power({0},{1}) returns: {2} ".format(1,1,is_power(1,1)))
    print("is_power({0},{1}) returns: {2} ".format(10,1,is_power(10,1)))
    print("is_power({0},{1}) returns: {2} ".format(3,3,is_power(3,3)))


is_power(10,2) returns: False 
is_power(27,3) returns: True 
is_power(1,1) returns: True 
is_power(10,1) returns: False 
is_power(3,3) returns: True 

############################# Good Answer ###############################


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_power(a, b):
    if a == 1 or b == 1:
# a more concise way to test base case
        return a == 1  
    return is_divisible(a, b) and is_power(a/b, b)
# The divisible and recursions will report either True or false

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))