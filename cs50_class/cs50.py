# from functions import square

# for i in range(10):
#     print(f"{i} squared is {square(i)}")

# if __name__ == "__main__":
#     main()


# Dictionary

ages = {"Alice": 22, "Bob": 27, "Mohamed": 35, "Hala": 25}

name = input("Who do you want to look up? ")

try:
    print(f"{name} is {ages[name]} years old.")

except KeyError:
    print(f"Sorry, {name} is not in the dictionary")
