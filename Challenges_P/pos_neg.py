# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if
# both are negative.


def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False
    elif (a < 0 and b > 0) or (a > 0 and b < 0):
        return True
    else:
        return False


###################### Another Answer ##################################
# def pos_neg(a, b, negative):
#     if negative:
#         return a < 0 and b < 0
#     else:
#         return (a < 0 and b > 0) or (a > 0 and b < 0)


print(pos_neg(1, -1, False))  # → True
print(pos_neg(-1, 1, False))  # → True
print(pos_neg(-4, -5, True))  # → True

