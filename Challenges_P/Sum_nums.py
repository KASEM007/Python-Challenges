# Write a method sum_nums(max) that takes in a number max and
# return the sum of all numbers  from 1 up to and including max?


def sum_nums(max):
    i = 1
    sum = 0

    while i <= max:
        sum = sum + i
        i += 1
    return sum


print(sum_nums(4))
print(sum_nums(5))
