import math
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     print('dsquared is', dsquared)
#     result = math.sqrt(dsquared)
#     return result

#print(distance(1, 2, 4, 6))

# part 1
# As an exercise, use incremental development to write a 
# function called [hypotenuse] that returns the length of 
# the [hypotenuse] of [a] right triangle given the lengths of 
# the other [two] => a, b legs as arguments. Record each stage of 
# the development process as you go.

# def hypotenuse(a, b):
#     answer = (a ** 2 + b ** 2)
#     return answer

# print(hypotenuse(3, 4))
    

# Another answer
# def distance (x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx ** 2 + dy ** 2
#     hypotenuse = math.sqrt(dsquared)
#     return hypotenuse

# D = distance(1, 2, 4, 6)
# print(D)

# Invent my own function
#Trying to build a function that will be able to count the average of 3 element
# to find the average we sum the element and then divided by the number of elment
def average_of_3(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum / 3
    return avg
    

    
print(average_of_3(2, 3, 4))
