# Given an array of integeras for example [1, 3, 4, 5, 0, 2]


# print(second_largest([1, 3, 4, 5, 0, 2]))  # should return 4.
# print(second_largest([-2, -1]))  # should return -2.
# print(second_largest([2, 2, 1]))  # should return 2.
# print(second_largest([2]))  # should return None.
# print(second_largest([]))  # should return None.

###########################################################
# Write note:
# print("#" * 80)
# print("You can write the full month or just the first letter: ".center(40, "#"))
# print("#" * 80)
# # collect age data
# age = input("What is your age? ").strip()

# # collect time unit
# unit = input("Please choose time unit: Months, Weeks, Days: ").strip().lower()

# # get time unit
# Months = int(age) * 12
# Weeks = Months * 4
# Days = int(age) * 365

# if unit == Months or unit == "M":

#     print("You Choosed the unit Months")
#     print(f"You lived for {Months:,} Months.")

# elif unit == Weeks or unit == "W":

#     print("You choosed the unit weeks")
#     print(f"You lived for {Weeks:,} weeks.")

# elif unit == Days or unit == "D":

#     print("You choose the unit Days")
#     print(f"You Lived for {Days:,} Days.")

#########################################################################
# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Type Your Name ").strip().capitalize()

# If Name is In Admin
if name in admins:

    print(f"Hello {name} Welcome Back")

    option = input("Delete Or Update Your Name ?").strip().capitalize()

    # Update Option
    if option == "Update" or option == "U":

        theNewName = input("Your New Name Please ").strip().capitalize()

        admins[admins.index(name)] = theNewName

        print("Name Updated.")

        print(admins)

    # Delete Option
    elif option == "Delete" or option == "D":

        admins.remove(name)

        print("Name Deleted")

        print(admins)

    # Wrong Option
    else:

        print("Wrong Option Choosed")

else:

    status = input("Not Admin, Add You Y, N ? ").strip().capitalize()

    if status == "Yes" or status == "Y":

        print("You Have Been Added")

        admins.append(name)

        print(admins)

    else:

        print("You Are Not Added.")

