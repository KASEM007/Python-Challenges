# What output will the following Python program produce?
n = 10
while n != 1:
    print (n,)
    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = n * 3 + 1

#What is the output of the Python method call below?

"bib".find('b', 1, 2)
# -1

# What does Python function subroutine do?

def subroutine( n ):
    while n > 0:
        print (n,)
        n = n - 1
        

#For the Python program below, will there be any output, and will the program terminate?

while True:

    while 1 > 0:

        break

    print("Got it!")

    break