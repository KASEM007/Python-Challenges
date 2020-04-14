# Tax Purchase

# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.


state = "NY"
purchase_amount = 220

if state == "CA":
    tax_amount = 0.075
    total_cost = purchase_amount * (1 + tax_amount)
    result = f"Since you're from {state}, your total cost is {total_cost}."
elif state == "MN":
    tax_amount = 0.095
    total_cost = purchase_amount * (1 + tax_amount)
    result = f"Since you're from {state}, your total cost is {total_cost}."

elif state == "NY":
    tax_amount = 0.089
    total_cost = purchase_amount * (1 + tax_amount)
    result = f"Since you're from {state}, your total cost is {total_cost}."

print(result)
