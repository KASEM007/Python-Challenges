###################################### part 1 ###################################################
# 1. Section 8.3 of Think Python.

prefixes = 'JKLMNOPQ'
suffix = 'ack'

# for letter in prefixes:
#      print(letter + suffix)

# Put this code into a Python script and run it. Notice that it prints the names "Oack" and "Qack".
# Modify the program so that it prints "Ouack" and "Quack" but leaves the other names the same.
# Include the modified Python code and the output in your submission.
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

for letter in prefixes: 
     if letter == "O":
         print(letter + "u" + suffix)
     elif letter == "Q":
         print(letter + "u" + suffix)
     else:
        print(letter + suffix)

###################################### part 2 ###################################################

# 2. Give at least three examples that show different features of string slices. Describe the feature 
# illustrated by each example. Invent your own examples. Do not copy them for the textbook or any other 
# source.

# example (1)
# uopeople = "University of the people"
# print("I am excited to join the " + uopeople)
# here we assign uopeople to the string[ University of the people ]
# so every time we use uopeople it will print the string [ University of the people ]

# example (2)
# people = "You don't have to be good at math to learn programing"
# book = " Think pyhton"
# reality = "You better be " + people[21:] + " from " + book[:]
# print(reality)
 # here I did slicing using the squar braket start with my starting point and then 
 # [start point: End point] then add my ending point if I leave the braket empty it
 # will add the whole sentence.

# example (3)
# print(uopeople.upper())
# Here we using the build in function .upper() to transfer  our sentence from lower case
# to upper case we also can use .lower() to do the opposite.