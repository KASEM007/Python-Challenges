# Given two strings, return True if either of the strings appears
# at the very end of the other string, ignoring upper/lower case
# differences (in other words, the computation should not be
# "case sensitive"). Note: s.lower() returns the lowercase version
# of a string.


def end_other(a, b):
    long_str = a.lower()
    short_str = b.lower()

    return long_str.endswith(short_str) or short_str.endswith(long_str)


print(end_other("Hiabc", "abc"))  # → True
print(end_other("AbC", "HiaBc"))  # → True
print(end_other("abc", "abXabc"))  # → True
print(end_other("abcXYZ", "abcDEF"))  # → False
