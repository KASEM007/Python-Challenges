# # BMI calculator
# name_1 = "Susu"
# name_2 = "Nada"
# name_3 = "Khaled"

# weight_kg1 = 90
# weight_kg2 = 70
# weight_kg3 = 160

# height_m1 = 90
# height_m2 = 70
# height_m3 = 160


# def bmi_calculator(name, height_m, weight_kg):
#     bmi = weight_kg / (height_m * height_m)
#     print("bmi: ")
#     print(bmi)

#     if bmi < 25:
#         return name + " is not overweight"
#     else:
#         return name + " is overweight"


# result_1 = bmi_calculator(name_1, height_m1, weight_kg1)
# result_2 = bmi_calculator(name_2, height_m2, weight_kg3)
# result_3 = bmi_calculator(name_3, height_m3, weight_kg3)

# print(result_1)
# print(result_2)
# print(result_3)


# ###########################################################################
# # height = float(input("Input your height in meters: "))
# # weight = float(input("Input your weight in kilogram: "))
# # print("Your body mass index is: ", round(weight / (height * height), 2))


# ###########################################################################
name = input("Enter your name: ")
height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in  klg: "))

bmi = weight / (height * height)

print(name + " BMI is: ", bmi)
