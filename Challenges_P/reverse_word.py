# write a method reverse(word) that takes in a string word and returns the word with its
# letters in reverse order.


def reverse(word):
    new_word = ""
    i = 0

    while i < len(word):
        char = word[i]
        new_word = char + new_word
        i += 1

    return new_word


print(reverse("cat"))
print(reverse("programing"))
print(reverse("bootcamp"))

