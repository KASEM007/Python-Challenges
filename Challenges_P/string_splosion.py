# Given a non-empty string like "Code" return a string like "CCoCodCode".


def string_splosion(str):
    result = ""
    # on each iteration, add  the substring of the chars 0..i
    for i in range(len(str)):
        result = result + str[: i + 1]
    return result


print(string_splosion("Code"))  # → 'CCoCodCode'
print(string_splosion("abc"))  # → 'aababc'
print(string_splosion("ab"))  # → 'aab'

