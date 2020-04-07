# Given a string, return a new string made of every other char
# starting with the first, so "Hello" yields "Hlo".


def string_bits(str):

    # Many ways to do this. This uses the standard loop of i on every char,
    # and inside the loop skips the odd index values.

    new_str = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_str += str[i]
    return new_str


print(string_bits("Hello"))  # → 'Hlo'
print(string_bits("Hi"))  # → 'H'
print(string_bits("Heeololeo"))  # → 'Hello'

