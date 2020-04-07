# is reverse:
# write a function compar two words and return True if one of the words
# is the reverse of the other one.
def is_reverse(word1, word2):

    if len(word1) != len(word2):
        return False
    i = 0
    x = len(word2) - 1
    while x < 0:
        if word1[i] != word2[i]:
            return False
        i = i + 1
        x = x - 1
    return True


print(is_reverse("pots", "stop"))
print(is_reverse("goo", "oog"))
print(is_reverse("google", "elgooge"))

############################### The in operator ##############################


# def in_both(word1, word2):
#     count = 0
#     for letter in word1:
#         if letter in word2:
#             count += 1
#     return count


# print(in_both("pots", "stop"))
# print(in_both("goo", "oog"))
# print(in_both("google", "elgooge"))
