def factorial(n):
    if n == 0:
        return 1
    else:
        x = factorial(n - 1)
        answer = n * x
        return (answer)
    
factorial(3)

