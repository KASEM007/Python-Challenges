# If you try to follow the flow of execution here, even for fairly small values of n, your head
# explodes. But according to the leap of faith, if you assume that the two recursive calls work
# correctly, then it is clear that you get the right result by adding them together.


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# If you played with the fibonacci function from Section 6.7, you might have noticed that
# the bigger the argument you provide, the longer the function takes to run. Furthermore,
# the run time increases quickly.
# To understand why, consider Figure 11.2, which shows the call graph for fibonacci with
# n=4:
# A call graph shows a set of function frames, with lines connecting each frame to the frames
# of the functions it calls. At the top of the graph, fibonacci with n=4 calls fibonacci with
# n=3 and n=2. In turn, fibonacci with n=3 calls fibonacci with n=2 and n=1. And so on.
# Count how many times fibonacci(0) and fibonacci(1) are called. This is an inefficient
# solution to the problem, and it gets worse as the argument gets bigger.
# One solution is to keep track of values that have already been computed by storing them
# in a dictionary. A previously computed value that is stored for later use is called a memo.
# Here is a “memoized” version of fibonacci:

known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


# known is a dictionary that keeps track of the Fibonacci numbers we already know. It starts
# with two items: 0 maps to 0 and 1 maps to 1.
# Whenever fibonacci is called, it checks known. If the result is already there, it can return
# immediately. Otherwise it has to compute the new value, add it to the dictionary, and
# return it.
