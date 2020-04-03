# Convert miles to kilometers

# miles = float(input('Enter distance in miles:'))


def main():
    miles = float(input("Enter distance in miles:"))
    conv_fac = 1.609344  # conversion factor
    # calculating how many kilometers
    kilometers = miles * conv_fac
    print("The distance in kilometers is:", kilometers)


main()


# def convert_to_kilo(miles):
#     return miles * 1.609344

# print(convert_to_kilo(6))

###################################################################
# Convert celsius to fahernheit:

# Take the temperature in degrees Celsuis and covert it to Fahernheit
# To covert degrees celsius temperature to Fahernheit, we have to mltiply
# by 9 and divided by 5 and then add 32

celsius = float(input("Enter temperature in degree Celsius:"))
fahernheit = celsius * 9 / 5 + 32
print("Temperature in Fahrenheit:", fahernheit)

