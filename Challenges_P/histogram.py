# histogram
# Write a function that takes a string and count
# how many times each charator appears.


def histogram(str):
    d = dict()
    for char in str:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


print(histogram("parrot"))
print(histogram("bootcamp"))

