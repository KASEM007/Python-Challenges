# if number is divisible by 3 return "Fizz"
# if number is divisible by 5 return "Buzz"
# if number divisible by both 3 and 5 return "Fizz buzz"
# if number is not diviable by both return the number it self
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 != 0 and num % 5 != 0:
        return num
    else:
        if num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
    

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(7))
print(fizz_buzz(15))