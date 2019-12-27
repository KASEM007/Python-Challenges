#map:    is operation that capitalize(select) all the element in the list.
#filter: is operation that selects some of the elements and filters out the others.
#reduce: is combines a sequence of elements into a single value is sometimes.

#################################### .append() #######################################

# adds a new element to the end of the list
t = ["a", "b", "c"]
t.append("d")
output["a", "b", "c", "d"]

t = ["a", "b", "d", "a", "z"]
def capitalize_all(t):
    new_list = []
    for i in t:
        new_list.append(i.capitalize())
    return new_list

print(capitalize_all(t))
# An operation like capitalize_all is sometimes called a map because it “maps” a function
# (in this case the method capitalize) onto each of the elements in a sequence.

# Another common operation is to select some of the elements from a list and return a sublist.
# For example, the following function takes a list of strings and returns a list that contains
# only the uppercase strings:

def only_upper(t):
    new_list =[]
    for i in t:
        if i.isupper():
            new_list.append(i)
    return new_list

# isupper is a string method that returns True if the string contains only upper case letters.
# An operation like only_upper is called a filter because it selects some of the elements and
# filters out the others.
# Most common list operations can be expressed as a combination of map, filter and reduce.

#################################### .extend() ########################################

#extend takes a list as an argument and appends all of the elements:
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> t1
['a', 'b', 'c', 'd', 'e']

###################################### .Sort() ########################################

#arranges the elements of the list from low to high:
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> t
['a', 'b', 'c', 'd', 'e']
# Most list methods are void; they modify the list and return None. If you accidentally write
# t = t.sort(), you will be disappointed with the result.      >>>(None)

* Make copies to avoid aliasing.
If you want to use a method like sort that modifies the argument, but you need to
keep the original list as well, you can make a copy.
>>> t = [3, 1, 2]
>>> t2 = t[:]
>>> t2.sort()
>>> t
[3, 1, 2]
>>> t2
[1, 2, 3]

In this example you could also use the built-in function sorted, which returns a new,
sorted list and leaves the original alone.
>>> t2 = sorted(t)
>>> t
[3, 1, 2]
>>> t2
[1, 2, 3]

######################################## sum() or reduce ##################################

#Adding up the elements of a list is such a common operation that Python provides it as a
#built-in function, sum:
>>> t = [1, 2, 3]
>>> sum(t)
6
#An operation like this that combines a sequence of elements into a single value is sometimes
#called reduce.

###################################### list() ########################################

# A string is a sequence of characters
# A list is a sequence of values, but a list of characters
#is not the same as a string. To convert from a string to a list of characters, you can use list:
>>> s = 'spam'
>>> t = list(s)
>>> t
['s', 'p', 'a', 'm']

###################################### .split() ########################################

# The list function breaks a string into individual letters. If you want to break a string into
# words, you can use the split method:
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> t
['pining', 'for', 'the', 'fjords']

###################################### .join() ########################################

#join is the inverse of split. It takes a list of strings and concatenates the elements. join is
#a string method, so you have to invoke it on the delimiter and pass the list as a parameter:
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> s = delimiter.join(t)
>>> s
'pining for the fjords'
#In this case the delimiter is a space character, so join puts a space between words. To
#concatenate strings without spaces, you can use the empty string, '', as a delimiter.

To add an element, you can use the append method or the + operator. Assuming that
t is a list and x is a list element, these are correct:

t.append(x)
t = t + [x]
t += [x]

And these are wrong:

t.append([x])            # WRONG!
t = t.append(x)          # WRONG!
t + [x]                  # WRONG!
t = t + x                # WRONG!

10.14 Glossary

list: A sequence of values.
element: One of the values in a list (or other sequence), also called items.
nested list: A list that is an element of another list.
accumulator: A variable used in a loop to add up or accumulate a result.
augmented assignment: A statement that updates the value of a variable using an operator
like +=.
reduce: A processing pattern that traverses a sequence and accumulates the elements into
a single result.
map: A processing pattern that traverses a sequence and performs an operation on each
element.
filter: A processing pattern that traverses a list and selects the elements that satisfy some
criterion.
object:     Something a variable can refer to. An object has a type and a value.
equivalent: Having the same value.
identical:  Being the same object (which implies equivalence).
reference:  The association between a variable and its value.
aliasing:   A circumstance where two or more variables refer to the same object.
delimiter:  A character or string used to indicate where a string should be split.

################################### Discussion forum unit 6 ##################################

1- Describe the difference between objects and values using the terms “equivalent” and “identical”. 
   Illustrate the difference using your own examples with Python lists and the “is” operator.

   car = "Tesla"
   electric_car = "Tesla"
      print(car is electric_car)
>>> True
   # we know that car an electric_car are equivalent but we don't know if they are identical
   # to find out if they are identical we can use the is operator

#In this example, Python only created one string object, and both car and electric_car refer to it. But
#when you create two lists, you get two objects:

        cars = ["Tesla", "Nissan", "Toyota"]
        electric_car = ["Tesla", "Nissan", "Toyota"]
    print(cars is electric_car)

>>> False
# If two objects are identical, they are also equivalent, but if they are equivalent, 
# they are not necessarily identical.

2- Describe the relationship between objects, references, and aliasing. 
  Again, create your own examples with Python lists.

  - Objects   is what the variable refer to list, string or integer.
  - Reference is the association of a variable with an object.
  - Aliasing  is an object with more than one reference has more than one name.

        car = ["Tesla", "Nissan", "Toyota"]
        electric_car = car
    print(electric_car is car)

>>> True

##################################### function #######################################
def e_cars(cars):
    electric_car = []
    for i in cars:
        
        if i[-1] == "e":
            electric_car.append(i)
    return electric_car

print(e_cars(["Tesla_e", "Nissan_e", "Toyota_e", "Nissan", "Toyota", "Honda"]))

>>> ['Tesla_e', 'Nissan_e', 'Toyota_e']

# def E_cars(e):
#     electric_car = []
#     i = 0
#     while i < len(e)-1:
#         if i[-1] == "e":
#             electric_car += i
#             i += 1
#     return electric_car

# print (E_cars["Tesla_e", "Nissan_e", "Toyota_e", "Nissan", "Toyota", "Honda"])

################################## Another Answer #################################


First, let's start with definitions:

Objects are memory location, with a specific size and type.

Values: are part of an object, and they can change, objects whose value is unchangeable 
        once they are created are called immutable.

Equivalent: object who have the same value, but referring to different memory locations

Identical: Object who are referring to the same memory location. which means that this is 
            the same object

in the next example we will define a few lists

 Class = ["ahmed", "jack", "john"] 

and

 Class2 = Class[:] 

those are two different objects, they share the same result there they are Equivalent.

 >>> Class == Class2
True 

yet both are referring to different addresses in memory, so they are not identical.

>>> Class2 is Class
False

let's assume we have three classes "Class3" and we referenced it to the same memory location 
that Class is referring to. now we have 3 Lists of the same values.

>>> Class3 = Class
>>> Class3
['ahmed', 'jack', 'john']
>>> 

Class and Class3 have the same memory location and they have the same Values. this makes the two 
objects identical.

>>> Class3 == Class
True
>>> Class3 is Class
True
>>> Class3 is Class2
False
>>> Class3 == Class2
True
>>>  ---

As I explained before, an object is any type of data that has a value. in this case, 
we have 3 list objects that have the same value. so they are all equivalent. but only Class and 
Class3 are identical because only Class and Class3 refer to the same object in memory. even though 
Class2 has the same values, it refers to a different object in memory.

________________

--- # a function that modifies a list of week days
week = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
month_day = week[:]
def week_month(week):
    for day in week:
        month_day[week.index(day)] = week.index(day)+16

def print_days():
    for i in range(7):
        print(week[i], month_day[i])


week_month(week)
print_days() ---

in this example we take the weekdays starting with Monday, then we take a new object to we 
reference it to a new copy of the week list to get a list with a length of 7. then we use 
the first for loop function week_month(week), that takes the first list as an argument and 
access each element of the second list month_day, which is the numeric representation of the 
day concerning the month and modifies it. now we are left with 2 lists, 1 for weekdays and another 
with the days of the month of that week.

then the other print_days() function prints each pay of the week with its corresponding day of the month.

the outcome would look as follow

Monday 16
Tuesday 17
Wednesday 18
Thursday 19
Friday 20
Saturday 21
Sunday 22
######################################################################################
######################################################################################
1. When two variables are assigned the same value, the assigned objects are then identical. 
    However, assigned values may be equivalent, but they are not necessarily identical, 
    so they contain different objects. Lists are an example of objects - equivalent values, 
    but not identical.
    Example of object being identical:

friday = "awsome"
weekend = "awsome"
friday is weekend
>>> true

The values assigned to Friday and Weekend are exactly the same, therefore when tested with 
the is operator, we receive a boolean value of True.

Example of objects being equivalent, but not identical like values are:

friday = ['awsome', 'amazing', 'fun']
weekend = ['awsome', 'amazing', 'fun']
friday is weekend
>>> False
Because lists contain objects rather than values, the use of the is operator returns 
a False boolean value.

2. Assigned object (list) to a name, 'Friday'.
    friday = ['awsome', 'amazing', 'fun']

The object assigned to the variable Friday is a list containing values ‘awesome’, ‘amazing’, ‘fun!’.
Next, we create another variable that references the object assigned to Friday. There is not another 
list created with the same values in the object, rather we simply refer to the list that is already created.  

friday = ['awsome', 'amazing', 'fun']
weekend = friday

Now, if we execute Weekend, we receive the list with the same objects as Friday. We have created 
an alias (or another name) for the original list using a reference.

friday = ['awsome', 'amazing', 'fun']
weekend = friday
>>> weekend
['awsome', 'amazing', 'fun']

################################# Learning Journal Unit 6 ###################################
                      ################### part 1 #########################

secret = "I love cars, so far tesla is my favorite for the last 3 years!"
x_secret = secret.split()

#  Delete(1)
delet_1_secret = x_secret.pop(1)
print(delet_1_secret)
>>> love

# Delete(2)
del x_secret[1]
print(x_secret)
>>>['I', 'cars,', 'so', 'far', 'tesla', 'is', 'my', 'favorite', 'for', 'the', 'last', '3', 'years!']

# Delete(3)
x_secret.remove('tesla')
print(x_secret)
>>>['I', 'cars,', 'so', 'far', 'is', 'my', 'favorite', 'for', 'the', 'last', '3', 'years!']   

secret = "I love cars, so far tesla is my favorite for the last 3 years!"
x_secret = secret.split()

# Add(1)
x_secret.append('and maybe alot more to come')
print(x_secret)


# Add(2)
add = ['from', ' future', 'electric', 'cars']
x_secret += add
print (x_secret)

# Add(3)
x_secret.insert(4, "I just love it")
print(x_secret)

# Join()
print(' '.join(x_secret))

                                                     ################### part 2 #########################

# Nested list

electric_cars = ['Toyota', 'Nissan', 'Honda', ['Tesla_3', 'Tesla_X', 'Tesla_Y'], 'BMW']
print(electric_car[3])
#>>> ['Tesla_3', 'Tesla_X', 'Tesla_Y']
# The "*" operator
print(2 * 3)
#>>> 6

# List slices
electric_cars = ['Toyota', 'Nissan', 'Honda', ['Tesla_3', 'Tesla_X', 'Tesla_Y'], 'BMW']
print(electric_cars[3:])
#>>>[['Tesla_3', 'Tesla_X', 'Tesla_Y'], 'BMW']

# The “+=” operator 
print(2 + 2)
>>> 4

#  list filter 

def e_cars(cars):
    electric_car = []
    for i in cars:
        
        if i[-1] == "e":
            electric_car.append(i)
    return electric_car

print(e_cars(["Tesla_e", "Nissan_e", "Toyota_e", "Nissan", "Toyota", "Honda"]))

#>>> ['Tesla_e', 'Nissan_e', 'Toyota_e']
# the e_cars is a filter because it selects some of the elements that ends with a letter "e" and
# filters out the others.


# A list operation that is legal but does the "wrong" thing, not what the programmer expects 
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print t
['a', 'c']
The return value from remove is None.



