# Basically, the function has to prompt the user to enter the first two letters
# of a day of the week and it should return the full worded day of the week.
# It should continue to prompt the user to do this until the user inputs an
# invalid two characters.


def abr():
    abbrev = input("Enter a day abbreviation:")
    days = {
        "Su": "Sunday",
        "Mo": "Monday",
        "Tu": "Tuesday",
        "We": "Wednesday",
        "Th": "Thursday",
        "Fr": "Friday",
        "Sa": "Saturday",
    }
    # if abr in days:
    #     return days[abr]
    # else:
    #     return None
    while True:
        if abr() == "":
            break


print(abr("Mo"))
