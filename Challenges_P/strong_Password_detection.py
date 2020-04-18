import re

password = re.compile(
    r"""(
    ^(?= .*[A-Z].*[A-Z])           # two capital letters
    (?= .* [! @ # $ & *])          # two special characters
    (?= .* [0-9].*[0.9])           # two numeric digits
    (?= .* [a-z].* [a-z].*[a-z]).{10,} # three lower case letter
    $                                       # atleast 10 total digits
    )""",
    re.VERBOSE,
)


def password_check():
    passw = input("Enter a Password: ")
    m = password.search(passw)
    if not m:
        print("Weak Password!")
        return False
    else:
        print("Strong Password")
        return True


password_check()
