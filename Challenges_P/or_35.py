# Return true if the given non-negative number is a multiple of
# 3 or a multiple of 5. Use the % "mod" operator


# def or_35(n):
#     return n % 3 == 0 or n % 5 == 0


# print(or_35(3))  # → true
# print(or_35(10))  # → true
# print(or_35(8))  # → false

##########################################################
# near_ten
# Given a non-negative number "num", return True if num is within 2 of
# a multiple of 10. Note: (a % b) is the remainder of dividing a by b,
# so (7 % 5) is 2.


def near_ten(num):

    # nums = [num - 2, num - 1, num, num + 1, num + 2]

    # for n in nums:
    #     if n % 10 == 0:
    #         return True
    # else:
    #     return False

    ### Another Answer
    # return abs(num % 10) in [0, 1, 2, 8, 9]

    ### Another Answer
    return num % 10 <= 2 or abs(num % 10 - 10) <= 2


print(near_ten(12))  # → True
print(near_ten(17))  # → False
print(near_ten(19))  # → True
print(near_ten(158))  # -> True

