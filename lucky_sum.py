# lucky_sum

# Given 3 int values, a b c, return their sum. However,
# if one of the values is 13 then it does not count towards
# the sum and values to its right do not count. So for example,
# if b is 13, then both b and c do not count.


def lucky_sum(a, b, c):
    total = [a, b, c]
    new_list = []
    for i in total:
        if i == 13:
            break
        else:
            new_list.append(i)
    return sum(new_list)


print(lucky_sum(1, 2, 3))  # → 6
print(lucky_sum(1, 2, 13))  # → 3
print(lucky_sum(1, 13, 3))  # → 1

