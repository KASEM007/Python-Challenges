# Problem 1:
# Here's Sample Interview Question number one with array or
# a Python list. Here's the problem: You're given an array or
# a Python list of integers. For example, [1, 2, 3, 4, 5, 0, 2],
# and I want you to write a function which takes the the given
# array and finds and returns the second largest number in this
# array. Let's call this function second largest.


def second_largest(given_list):
    largest = None
    second_largest = None

    for current_number in given_list:
        if largest == None:
            largest = current_number
        elif current_number > largest:
            second_largest = largest
            largest = current_number
        elif second_largest == None:
            second_largest = current_number
        elif current_number > second_largest:
            second_largest = current_number
    return second_largest


print(second_largest([1, 3, 4, 5, 0, 2]))  # 4
print(second_largest([-2, -1]))  # -2
print(second_largest([2, 2, 1]))  # 2
print(second_largest([2]))  # None
print(second_largest([]))  # None

