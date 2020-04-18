# Your flower match:
# Create a function that opens the flowers.txt,
# reads every line in it, and saves it as a dictionary.
# The main (separate) function should take user input
# (user's first name and last name) and parse the user
# input to identify the first letter of the first name.
# It should then use it to print the flower name with
# the same first letter
# (from dictionary created in the first function).

# Write your code here

# HINT: create a dictionary from flowers.txt
def creat_flower_dict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict


# HINT: create a function to ask for user's first and last name
# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main():
    flower_d = creat_flower_dict("flowers.txt")
    full_name = input("Enter your First [space] last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]


# print command that prints final input with value
# from corresponding key in dictionary
print(f"Unique flower name with the first letter: {flower_d[first_letter]}")

# print the desired output
