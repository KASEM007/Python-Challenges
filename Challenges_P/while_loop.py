
############################################# While Loop #############################################

# def count_down(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print('Blastoff!')


# def count_up(n):
#     while n < 0:
#         print (n)
#         n = n + 1
#     print('Blastoff!')


# def count(n):
#     if n < 0:
#         count_up(n)
#     elif n > 0:
#         count_down(n)
#     else:
#         print("Number can't be Zero!. Please try again")

############################################# Recursion #############################################

# def count_down(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         count_down(n - 1)


# def count_up(n):
#     if n >= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         count_up(n + 1)



# def count(n):
#     if n < 0:
#         count_up(n)
#     elif n > 0:
#         count_down(n)
#     else:
#         print("Number can't be Zero!. Please try again")
        
# count(3)
# count(-3)
#count(0)


############################################# Another While loop ######################################

fruit = "bannana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (letter)
    index = index + 1

