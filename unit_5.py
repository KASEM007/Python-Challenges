# Think pyhton

# def in_both(word1, word2):
#     for letter in word1:
#         if letter in word2:
#             print(letter      )


# in_both("apples", "oranges")

# def is_reverse(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     i = 0
#     j = len(word2) - 1
#     while j > 0:
#         print(i, j)
#         if word1[i] != word2[j]:
#             return False
#         i = i + 1
#         j = j - 1
#     return True

# print(is_reverse('pots', 'stop'))

############################################# Exercise 8.4 #####################################

# This assignment is based on Exercise 8.4 from your textbook. Each of the following Python
# functions is supposed to check whether its argument has any lowercase letters.
# For each function, describe what it actually does when called with a string argument. 
# If it does not correctly check for lowercase letters, give an example argument that 
# produces incorrect results, and describe why the result is incorrect.

# (1)
# This one does check for lowercase letters, but it is checking the entire word. 
# It will only return true if all letters are lowercase.

# def any_lowercase1(s):
#     for c in s: 
#         if c.islower():  
#             return True
#         else:
#             return False

# print(any_lowercase1('Apple'))
# print(any_lowercase1('apple'))
# print(any_lowercase1('APPLE'))
# print(any_lowercase1('45e'))


# This function works great it check for every c = character and s = string
# the function check in each c in s if any of the letters is not a lower case
# it return False, if all the latter is lower case the it will return True
##### Another Answer

def any_lowercase1(s):
    for c in s:          # look at each letter c in string(s)
        if c.islower():  # if C is lowercase, return Boolean True
            return True
        else:             # if not, return False
            return False

print(any_lowercase1('Apple'))
print(any_lowercase1('applE'))
print(any_lowercase1('aPPLE'))
print(any_lowercase1('45e'))
# When called with a string argument('s'), function any_lowercase1(s) checks to see if c is lowercase.
#in this instance, c refers only the first letter of the stringas it will not loop beyond the first letter
# not the entire argument, whitch did have lowercase letters.

# (2)
# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             print(c)
#             return 'True'
#         else:
#             return 'False'

# print(any_lowercase2('apple'))
# print(any_lowercase2('Apple'))
# print(any_lowercase2('APPLE'))
# print(any_lowercase2('45'))
# here is the resualt is incorrect because the function is checking for the string 'c'
# and returning the string 'True' so the function just returning the first string without 
# checking for anything.

# (3)
# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
        
#     return flag

# print(any_lowercase3('apple'))
# print(any_lowercase3('Apple'))
# print(any_lowercase3('APPLE'))
# print(any_lowercase3('45e'))
# here is the resault is wrong because the function checking if any letter of the string 
# is lower case it will turn True no matter what and where that letter is as long as there 
# is a 1 lower case in the string it will return True

# (4)
# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag

# print(any_lowercase4('apple'))
# print(any_lowercase4('Apple'))
# print(any_lowercase4('APPLE'))
# print(any_lowercase4('45e'))
# This on is not really clear to me, because when i saw flag assign to False I thought
# that False will not be a boolian operator, but it is giving me the same resualt as before

#(5)

# def any_lowercase4(s):
#     for c in s:
#         if not c.islower():
#             return False
#     return True


# print(any_lowercase4('apple'))
# print(any_lowercase4('Apple'))
# print(any_lowercase4('APPLE'))
# print(any_lowercase4('45e'))

# This one works fine ass well as the first one, here the function check each letter (c)
# in the string (s) if any of the letter is not a lower case then it return False
# after the function iterate through the string if it didn't find any  not lower case
# it will retrun true at the end.