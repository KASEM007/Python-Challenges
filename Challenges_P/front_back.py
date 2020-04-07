# Given a string, return a new string where the
# first and last chars have been exchanged.


def front_back(str):
    new_str = ""
    first = str[0]
    last = str[-1]
    mid = str[1:-1]
    new_str = last + mid + first
    if len(str) < 2:
        return str
    else:
        return new_str


# def front_back(str):
#   if len(str) <= 1:
#     return str

#   mid = str[1:len(str)-1]  # can be written as str[1:-1]

#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]

print(front_back("code"))  # → 'eodc'
print(front_back("a"))  # → 'a'
print(front_back("ab"))  # → 'ba'

