# readable_timedelta
# Write a function named readable_timedelta.
# The function should take one argument, an integer days,
# and return a string that says how many weeks and days that is.
# For example, calling the function and printing the result like this:
# print(readable_timedelta(10))
# should output the following:
# 1 week(s) and 3 day(s).


def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return f"{weeks} week and {remainder} days."


print(readable_timedelta(10))
