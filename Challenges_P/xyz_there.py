# Return True if the given string contains an appearance of "xyz"
# where the xyz is not directly preceeded by a period (.). So "xxyz"
# counts but "x.xyz" does not.


def xyz_there(str):
    if len(str) < 3:
        return False

    for i in range(len(str)):
        if str[i - 1] != ".":
            if str[i : i + 3] == "xyz":
                return True
    else:
        return False


################ Another Answer ##################


# def xyz_there(str):
#     i = 0
#     while i < len(str):
#         if str[i - 1] != ".":
#             if str[i : i + 3] == "xyz":
#                 return True
#         i += 1
#     else:
#         return False


print(xyz_there("abcxyz"))  # → True
print(xyz_there("abc.xyz"))  # → False
print(xyz_there("xyz.abc"))  # → True

