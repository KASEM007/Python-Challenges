########################## Example 1 #######################
# def factorial(n):
#     if n == 0:
#         return (1)
#     else:
#         x = n - 1
#         answer = n * x
#         return (answer)

# print(factorial(3))

######################### Example 2 (recursion)################

# def factorial(n):
#     #if not isinstance(n, int):
#     if n < 0:
#         print('Factorial is only defined for negative integers.')
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(3))

######################### Example 3 (recursion) #########################

# An example of a recursive function to
# find the factorial of a number
# def clac_factroial(x):
#     """This is a recursive function to find the
#     factorial of an integer"""
#     if x == 1:
#         return 1
#     else:
#         return x * clac_factroial(x - 1)


# num = 4
# print("The factorial of", num, "is", clac_factroial(num))

# In the above example, calc_factorial() is a recursive functions as
# it calls itself.
# When we call this function with a positive integer, it will recursively
# call itself by decreasing the number.
# Each function call multiples the number with the factorial of number
# 1 until the number is equal to one. This recursive call can be explained
# in the following steps.

# calc_factorial(4)  # 1st call with 4
# 4 * calc_factorial(3)  # 2nd call with 3
# 4 * 3 * calc_factorial(2)  # 3rd call with 2
# 4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
# 4 * 3 * 2 * 1  # return from 4th call as number=1
# 4 * 3 * 2  # return from 3rd call
# 4 * 6  # return from 2nd call
# 24  # return from 1st call

# Our recursion ends when the number reduces to 1. This is called
# the base condition.
# Every recursive function must have a base condition that stops the
# recursion or else the function calls itself infinitely.

# Advantages of Recursion
# 1- Recursive functions make the code look clean and elegant.
# 2- A complex task can be broken down into simpler sub-problems using recursion.
# 3- Sequence generation is easier with recursion than using some nested iteration.

# Disadvantages of Recursion
# 1- Sometimes the logic behind recursion is hard to follow through.
# 2- Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
# 3- Recursive functions are hard to debug.

############################ Example 4 ############################

# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n - 1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result

# print(factorial(4))

############################ Example 4 ############################
# def factorial(num):
#     fact = 1
#     while num > 0:
#         # fact = [1, 4, 12, 24, 24]
#         # num = [3, 3, 2, 1]
#         fact = fact * num
#         num = num - 1
#     return fact


# print(factorial(4))


############################ Example 5 ############################

# Write a method factorial(num)that takes in a number num and returns
# the product of all numbers from 1 up to and including num?


def factorial(num):
    i = 1  # because any number multiply by 0  will be 0
    product = 1
    while i <= num:
        product *= i
        i += 1
    return product


print(factorial(3))  # because 1 * 2 * 3 = 6
print(factorial(5))  # because 1 * 2 * 3 * 4 * 5 = 120

