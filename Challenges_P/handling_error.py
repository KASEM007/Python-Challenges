# Handling Input Errors:

# The party_planner function below takes as input a number of
# party people and cookies and figures out how many cookies each
# person gets at the party, assuming equitable distribution of cookies.
# Then, it returns that number along with how many cookies will be left over.

# Right now, calling the function with an input of 0 people will cause
# an error, because it creates a ZeroDivisionError exception.
# Edit the party_planner function to handle this invalid input.
# If it runs into this exception, it should print a warning message
# to the user and request they input a different number of people.


def party_planner(cookies, people):
    left_overs = None
    num_each = None
    # TODO: Add a try-except block here to
    # make sure no Zero Division Error occurs
    try:
        num_each = cookies // people
        left_overs = cookies % people

    except ZeroDivisionError:
        print("\nOops, you enterd 0 people will be attending.")
        print("Please, enter a good number of people for party.")

    return (num_each, left_overs)


# THIS is the mean code block, do not edit:
lets_party = "y" or "Yes".lower()
while lets_party == "y" or "Yes".lower():
    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, left_overs = party_planner(cookies, people)

    if cookies_each:  # if cookies each is not None
        message = f"\n Let's party! we'll have {people} people attending,\n they'll each get to eat {cookies_each} cookies,\n and we'll have {left_overs} left over."

        print(message)

    lets_party = input("\n would you like to party more? (y or n) ")
