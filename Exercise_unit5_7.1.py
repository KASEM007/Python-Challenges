# Think python - Exercise 7.1.
# * part 1
# Encapsulate the following Python code from Section 7.5 in a function named my_sqrt 
# that takes a as a parameter, chooses a starting value for x, and returns an estimate 
# of the square root of a.

# a = 4
# x = 3
# y = (x + a/x) / 2
# print(y)
# while True:
#     print(x)
#     y = (x + a/x) / 2.0
#     if y == x:
#         break
#     x = y 
# if abs(y - x) < epsilon:
#     break
# Where [espilon] has a value like 0.0000001 that determines how close is clode enough.

# def my_sqrt(a):
#     x = a / 5
#     while True:
#         y = (x + a/x) / 2.0
#         if y == x:
#             return x
#         x = y

# print(my_sqrt(6))


##############################################################################################
#################################  part (2)  #################################################

# Write a function named test_sqrt that prints a table like the following using a while loop, 
# where "diff" is the absolute value of the difference between my_sqrt(a) and math.sqrt(a). 

# Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
# that takes a as a parameter, chooses a reasonable value of x, and returns an
# estimate of the square root of a.
# To test it, write a function named test_square_root that prints a table like this:
# a   mysqrt(a)      math.sqrt(a)   diff
# -   ---------      ------------   ----
# 1.0 1.0            1.0            0.0
# 2.0 1.41421356237  1.41421356237  2.22044604925e-16
# 3.0 1.73205080757  1.73205080757  0.0
# 4.0 2.0            2.0            0.0
# 5.0 2.2360679775   2.2360679775   0.0
# 6.0 2.44948974278  2.44948974278  0.0
# 7.0 2.64575131106  2.64575131106  0.0
# 8.0 2.82842712475  2.82842712475  4.4408920985e-16
# 9.0 3.0            3.0            0.0

##############################################################################################

# Write a function named test_sqrt that prints a table like the following using a while loop, 
# where "diff" is the absolute value of the difference between my_sqrt(a) and math.sqrt(a). 

# a = 1 | my_sqrt(a) = 1 | math.sqrt(a) = 1.0 | diff = 0.0
# a = 2 | my_sqrt(a) = 1.41421356237 | math.sqrt(a) = 1.41421356237 | diff = 2.22044604925e-16
# a = 3 | my_sqrt(a) = 1.73205080757 | math.sqrt(a) = 1.73205080757 | diff = 0.0
# a = 4 | my_sqrt(a) = 2.0 | math.sqrt(a) = 2.0 | diff = 0.0
# a = 5 | my_sqrt(a) = 2.2360679775 | math.sqrt(a) = 2.2360679775 | diff = 0.0
# a = 6 | my_sqrt(a) = 2.44948974278 | math.sqrt(a) = 2.44948974278 | diff = 0.0
# a = 7 | my_sqrt(a) = 2.64575131106 | math.sqrt(a) = 2.64575131106 | diff = 0.0
# a = 8 | my_sqrt(a) = 2.82842712475 | math.sqrt(a) = 2.82842712475 | diff = 4.4408920985e-16
# a = 9 | my_sqrt(a) = 3.0 | math.sqrt(a) = 3.0 | diff = 0.0 

# Modify your program so that it outputs lines for a values from 1 to 25 instead of just 1 to 9. 
#import math
# def mysqrt(a):
#     x = a/5
#     while True:
#         y = (x + a/x) / 2
#         if y == x:
#             return x
#         x = y

# def test_sqrt(a):
#     a = 1
#     x = a / 5
#     print("a         mysqrt(a) = 1        math.sqrt(a) = 1.0          diff = 0.0")
#     print("-         ---------        ------------          -----")
#     while a > 26:
#         print(eval(" a, "|", mysqrt(a), "|",   math.sqrt(a)   "|",       mysqrt(a) - math.sqrt(a)"))
#         a += 1

#print(test_sqrt(5))

# def mysqrt(a):
#     x = a/5
#     while True:
#         y = (x + a/x) / 2
#         if y == x:
#             return x
#         x = y
# import math
# def test_sqrt():
#     a = 1.0
#     print("'a' , repr(mysqrt(a)).rjust(6), repr(math.sqrt(a)).rjust(12), 'dif'.rjust(10)")
#     print(' -    ------------           --------------           ------------ ')
#     while a < 26:
#         print(eval(" a, ' | ', mysqrt(a), ' | ', math.sqrt(a), ' | ', abs(mysqrt(a)-math.sqrt(a))"))
#         a += 1
# print(test_sqrt())

##################################################################################
##################################################################################

# def mysqrt(a):
# 	epsilon = 0.00001
# 	x = 5.00000
# 	while True:
# 		y = (x + a/x) / 2
# 		if abs(y - x) < epsilon:
# 			return y
# 			break
# 		x = y
		
# import math
# print mysqrt( 4 )

# def test_square_root():
# 	print "a	mysqrt(a)	math.sqrt(a)	diff"
# 	print "-	---------	------------	----"
# 	for a in range(1, 26):
#             print ("%.1f	%.5f	        %.5f	        %f" % (a,mysqrt(a), math.sqrt(a), mysqrt(a)-math.sqrt(a)))
#             print ("a	mysqrt(a)	math.sqrt(a)	diff")		
# test_square_root()

##############################################################################################
#################################  Another Answer  ############################################

# import math

# def my_sqrt(a):
#     x = a/2
#     while True:
#         estimated_root = (x + a/x) / 2
#         if estimated_root == x:
#             return estimated_root
#             break
#         x = estimated_root

# def test_square_root(values_of_a):

#     linea = "a"
#     lineb = "my_sqrt(a)"
#     linec = "math.sqrt(a)"
#     lined = "diff"
    
#     line2a = "--"
#     line2b = "---------"
#     line2c = "------------"
#     line2d = "-----"
    
#     spacing1 = "  "
#     spacing2 = "       " 
#     spacing3 = "       "  
#     print(linea, spacing1, lineb, spacing2, linec, spacing3, lined)
#     print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)
    
#     for a in values_of_a:
#         cola = float(a)
#         colb = my_sqrt(a)
#         colc = math.sqrt(a)
#         cold = abs(my_sqrt(a) - math.sqrt(a))

#         print(cola, "{:<20f}".format(colb), "{:<20f}".format(colc), cold)

# test_square_root(range(1,26))

##############################################################################################
#################################  Another Answer  ######################################

# this function take a a paramenter as an argument,
# then puts it in a math equation many times until the value of a is equal to x

# import math

# def my_sqrt(a):
#     x = 2.0
#     while True:
#         y = (x + a/x) / 2.0
#         if y == x:
#             return y
#             break
#         x = y

# def test_sqrt():
#     a = 1
#     while a <= 25:
#         my = my_sqrt(a)
#         m = math.sqrt(a)
#         print("a =",a, "| my_sqrt(a) =" ,"%11.10f"% my, " | math.sqrt(a) =", "%11.10f"% m, "diff = ", my-m)
#         a = a+1
# test_sqrt()

#########################################################################################
#################################  The best Answer  ######################################

import math
def mysqrt(a):
	x = a
	while True:
		y = (x + a/x) / 2.0
		if y == x:
			break
		x = y
	return x
def test_square_root():
	a = 1
	while a < 26:
		mine = mysqrt(a)
		maths = math.sqrt(a)
		print("a =", a, "| mysqrt(a) =", mine, "| math.sqrt(a) =", maths, "| diff =", abs(mine-maths))
		a = a + 1

test_square_root()

