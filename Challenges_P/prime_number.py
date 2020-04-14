# Check for Prime Numbers:
# Prime numbers are whole numbers that have only two factors:
# 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

# For instance, 6 has four factors: 1, 2, 3, 6.
# 1 X 6 = 6
# 2 X 3 = 6
# So we know 6 is not a prime number.

# In the following coding environment, write code to check if
# the numbers provided in the list check_prime are prime numbers.

# If the numbers are prime, the code should
# print "[number] is a prime number."
# If the number is NOT a prime number, it should
# print "[number] is not a prime number",
# and a factor of that number, other than 1 and the number itself:
# "[factor] is a factor of [number]".

check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

    # search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

        # number is not prime if modulo is 0
        if (num % i) == 0:
            print(f"{num} is NOT a prime number, because {i} is a factor of {num}.")
            break

        # otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num - 1:
            print("{} IS a prime number".format(num))
