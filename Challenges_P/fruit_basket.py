###################### Fruit Basket - Task 1 ##########################

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and
# list of fruits. Use the dictionary and list to count the total
# number of fruits, but you do not want to count the other items
# in your basket.

result_1 = 0
basket_items = {"apples": 4, "oranges": 19, "kites": 3, "sandwiches": 8}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]


for key, value in basket_items.items():
    if key in fruits:
        result_1 += value

print(f"There is {result_1} fruits in the basket.")


###################### Fruit Basket - Task 2 ##########################

# If your solution is robust, you should be able to use it with any
# dictionary of items to count the number of fruits in the basket.
# Try the loop for each of the dictionaries below to make sure it
# always works.

# Example 1

result_2 = 0
basket_items = {"pears": 5, "grapes": 19, "kites": 3, "sandwiches": 8, "bananas": 4}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result_2 += value

print(f"There is {result_2} fruits in the basket.")

# Example 2

result_3 = 0
basket_items = {"peaches": 5, "lettuce": 2, "kites": 3, "sandwiches": 8, "pears": 4}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result_3 += value

print(f"There is {result_3} fruits in the basket.")


# Example 3

result_4 = 0
basket_items = {"lettuce": 2, "kites": 3, "sandwiches": 8, "pears": 4, "bears": 10}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result_4 += value

print(f"There is {result_4} fruits in the basket.")

###################### Fruit Basket - Task 3 ##########################

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {"apples": 4, "oranges": 19, "kites": 3, "sandwiches": 8}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Iterate through the dictionary
for key, value in basket_items.items():
    if key in fruits:  # if the key is in the list of fruits, add to fruit_count.
        fruit_count += value
    else:
        if (
            key not in fruits
        ):  # if the key is not in the list, then add to the not_fruit_count
            not_fruit_count += value


print(
    f"The number of fruit is {fruit_count} and there are {not_fruit_count} object that are not fruits."
)
