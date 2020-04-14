# Creat Usernames:

# Write a for loop that iterates over the names list to create a usernames list.
# To create a username for each name, make everything lowercase and replace spaces
# with underscores. Running your for loop over the list:

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should creat the list:
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

# write your for loop here

# usernames = []

# for i in names:
#     if " " in i:
#         i = i.replace(" ", "_").lower()
#     usernames.append(i)
# print(usernames)

###################### Modify Usernames with Range ##########################

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(names)):
    names[i] = names[i].lower().replace(" ", "_")

print(names)
