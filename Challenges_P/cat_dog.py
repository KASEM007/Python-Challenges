
# Cat_dog
#__________
# Return True if the string "cat" and "dog" appear the same number
# of times in the given string.


def cat_dog(str):
    count_cat = 0
    count_dog = 0

    for i in range(len(str) - 1):
        if str[i : i + 3] == "cat":
            count_cat += 1
        if str[i : i + 3] == "dog":
            count_dog += 1
    if count_cat == count_dog:
        return True
    else:
        return False



print(cat_dog("catdog"))  # → True
print(cat_dog("catcat"))  # → False
print(cat_dog("1cat1cadodog"))  # → True

