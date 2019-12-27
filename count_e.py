# Count E
#  Write a function count_e(word) that takes in a string word 
#  and return the number of e's in the word

# def count_e(word):
#     count = 0
#     i = 0
#     while i < len(word):
#         char = word[i]
#         if char == "e":
#             count += 1
#         i += 1
#     return count

# print(count_e("movie"))
# print(count_e("excellent"))

############################################# Another function #####################################

# Count A and a
# Write a function count_a(word) that takes in a string word and returns the number
# of a's in the word. The function shloud count both lowercase (a) and uppercase(A).

# def count_a(word):
#     i = 0
#     count = 0
#     while i < len(word):
#         char = word[i]
#         if char == "a" or char == "A":
#             count += 1
#         i += 1

#     return count
 
# print(count_a("application"))
# print(count_a("pike"))
# print(count_a("Aardvark"))


############################################# Another function #####################################

# word = "banana"
# count = 0
# for letter in word:
#     if letter == 'a':
#         count += 1
#     print(count)

# # As an exercise, encapsulate this code in a function named count, and generalize it so that
# # it accepts the string and the letter as arguments.

# def count(string):
#     count = 0
#     for i in string:
#         if i == "a":
#             count += 1
#     print(count)

# count("aysha")

##################################### Another Function #####################################

# i = 0
# while i < 10:
#     if i % 2 == 0:
#         print (i)
#     i += 1
# print('We have 4 even numbers')
    
count = 0    
for i in range (1, 10):
    if i % 2 == 0:
        count += 1
        print (i)
    
print(f"we have {count} even number")