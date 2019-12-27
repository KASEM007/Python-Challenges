#########################      Recursion       #####################################
######################### Think python - unit 4 #####################################
# Do Exercise 6.4 from your textbook using recursion and the is_divisible function 
# from Section 6.4.  Your program may assume that both arguments to is_power are 
# positive integers. Note that the only positive integer that is a power of "1" is "1" itself.
# Return True if x is divisible by y, otherwiae False
# def is_divisible(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False

# Return True if a is an integer power of b, otherwise False
# Expects both arguments to be nonzero.
# def is_power(a, b):
#     if a == b: # base case where a/b == 1
#         return True
#     elif b == 1: # base case where a == 1 but does not
#         return False
#     else:
#         return is_divisible(a, b) and is_power(a/b, b)
# After writing your is_power function, include the following test cases in your 
# script to exercise the function and print the results:

# print("is_power(10, 2) returns: ", is_power(10, 2))
# print("is_power(27, 3) returns: ", is_power(27, 3))
# print("is_power(1, 1)  returns: ", is_power(1, 1))
# print("is_power(10, 1) returns: ", is_power(10, 1))
# print("is_power(3, 3)  returns: ", is_power(3, 3))

# Your submission will be assessed using the following Aspects.
# Does the submission include the is_divisible function from Section 6.4 of the textbook?
# Does the submission implement an is_power function that takes two arguments?
# Does the is_power function call is_divisible?
# Does the is_power function call itself recursively?
# Does the is_power function include code for the base case of the two arguments being equal?
# Does the is_power function include code for the base case of the second argument being "1"?
# Does the submission include correct output for the five test cases?
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_power(a, b):
    if a == b: # base case where a/b == 1
        return True
    elif b == 1: # base case where b == 1 but [a] does not
        return False
    else:
        return is_divisible(a, b) and is_power(a/b, b)

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1)  returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3)  returns: ", is_power(3, 3))
