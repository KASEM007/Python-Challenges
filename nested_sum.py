# Write a function called nested_sum that takes a nested list of integers
# and add up the elements from all of the nested lists.

#     # nestedList: list composed of nested lists containing int.
#     # Returns the sum of all the int in the nested list


def add_all(t):
    total = 0
    for i in t:
        if type(i) == list:  # check whether i is list or not
            total = total + add_all(i)
        else:
            total += i
    return total


print(add_all([13, 4, 5, 6, 8, [3, 4, 5], 4, 2, 1]))
