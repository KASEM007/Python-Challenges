# points = 174

# if points <= 50:
#     result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#     result = "Oh dear, no prize this time."
# elif points <= 180:
#     result = "Congratulations! You won a wafer-thin mint!"
# else:
#     result = "Congratulations! You won a penguin!"

# print(result)

############## Different way give same result ###################

# points = 174  # use this as input for your submission

# # establish the default prize value to None
# prize = None

# # use the points value to assign prizes to the correct prize names
# if points <= 50:
#     prize = "wooden rabbit"
# elif 151 <= points <= 180:
#     prize = "wafer-thin mint"
# elif points >= 180:
#     prize = "pinguin"

# # use the truth value of prize to assign result to the correct prize
# if prize:
#     result = f"Congratulation! You won a {prize}!"
# else:
#     result = "Oh dear, no prize this time"


# print(result)

########################## for loops ##############################

# cities = ["new york", "mountin view", "chicago", "los angeles"]

# # -(1)
# # for city in cities:
# #     print(city.title())

# # -(2)
# # capitalized_cities = []
# # for city in cities:
# #     capitalized_cities.append(city.title())

# # -(3)
# for i in range(len(cities)):
#     # cities[i] = cities[i].title()
#     print(cities[i].title())

########################## While loops ##############################

# card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
# hand = []

# # adds the last element of the card_deck list to the hand list
# # until the values in hand add up to 17 or more

# while sum(hand) <= 17:
#     hand.append(card_deck.pop())

# print(hand)


########################## Break ##############################

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
    print(f"current weight: ({weight})")
    if weight >= 100:
        break
    elif weight + cargo_weight > 100:
        print(f" skipping {cargo_name} ({cargo_weight})")
        continue
    else:
        print(f" adding {cargo_name} ({cargo_weight})")
        items.append(cargo_name)
        weight += cargo_weight

print(f"\nFinal Weight: {weight}.")
print(f"Final Items: {items}")
