# Example 1
# def factorial(n):
#     if n == 0:
#         return (1)
#     else:
#         x = n - 1
#         answer = n * x
#         return (answer)

# print(factorial(3))

# Example 2*****

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

# Example 3

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result

print(factorial(4))