# Return the number of times that the string "hi" appears
# anywhere in the given string.


def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] == "h" and str[i + 1] == "i":
            count += 1
    return count


################## Another Answer #################

# def count_hi(str):

#   i = 0
#   count = 0
#   while i < len(str)-1:
#     if str[i] == 'h' and str[i + 1] == 'i':
#       count += 1
#     i += 1
#   return count


print(count_hi("abc hi ho"))  # → 1
print(count_hi("ABChi hi"))  # → 2
print(count_hi("hihi"))  # → 2

