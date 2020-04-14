# Cargo Loading Program

# manifest = [
#     ("banans", 15),
#     ("mattresses", 34),
#     ("dog kennels", 42),
#     ("machine", 120),
#     ("cheeses", 5),
# ]

# weight = 0
# items = []

# for cargo in manifest:
#     # debugging print statment
#     print(f"current weight: {weight}.")
#     if weight >= 100:
#         break
#     else:
#         # debugging print statment
#         print(f"adding {cargo[0]} => ({cargo[1]})")
#         items.append(cargo[0])
#         weight += cargo[1]

# print(weight)
# print(items)

############################### Better solution Design ##########################

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit

manifest = [
    ("banans", 15),
    ("mattresses", 34),
    ("dog kennels", 42),
    ("machine", 120),
    ("cheeses", 5),
]

weight = 0
items = []

for cargo_name, cargo_weight in manifest:
    # debugging print statment
    # print(f"current weight: ({weight})")
    if weight >= 100:
        break
    elif weight + cargo_weight > 100:
        # debugging print statment
        # print(f" skipping {cargo_name} ({cargo_weight})")
        continue
    else:
        # debugging print statment
        # print(f" adding {cargo_name} ({cargo_weight})")
        items.append(cargo_name)
        weight += cargo_weight

print(f"\nFinal Weight: {weight}.")
print(f"Final Items: {items}")


#####################################################

# fruit = ["orange", "strawberry", "apple"]
# foods = ["apple", "apple", "hummus", "toast"]

# fruit_count = 0
# for food in foods:
#     if food not in fruit:
#         print("Not a fruit")
#         continue
#     fruit_count += 1
#     print("found a fruit!")

# print("Total fruit: ", fruit_count)
