# Extract First Names
# Use a list comprehension to create a new list first_names containing
# just the first names in names in lowercase.

# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# write your list comprehension here
# new_name = []
# first_name = []
# for name in names:
#     new_name.append(name.split())
# for x, y in new_name:
#     first_name.append(x.lower())

# print(first_name)

####################################### Better Way ###################################

# first_names = [name.split()[0].lower() for name in names]

# print(first_names)

####################################### Another Chanllenge ################################
# #                                      Multiples of Three:

# # Use a list comprehension to create a list multiples_3
# # containing the first 20 multiples of 3.

# multiples_3 = [x * 3 for x in range(1, 21)]

# print(multiples_3)


####################################### Another Chanllenge ################################
#                                     Filter Names by Scores:

# Use a list comprehension to create a list of names passed that only include those
# that scored at least 65.

scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98,
}
# write your list comprehension here
passed = [x for x, y in scores.items() if y >= 65]
print(passed)
