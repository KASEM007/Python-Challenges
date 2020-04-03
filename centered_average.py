# Centered_average
# Return the "centered" average of an array of ints,
# which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array.
# If there are multiple copies of the smallest value, ignore just
# one copy, and likewise for the largest value. Use int division
# to produce the final average. You may assume that the array is
# length 3 or more.


def centered_average(nums):
    # find the sum of the list and subtract the largest and smallest
    # elements then divide that by the length of the list minus 2.
    sum = 0
    max_value = max(nums)
    min_value = min(nums)

    for i in range(len(nums)):
        sum = sum + nums[i]

    return (sum - max_value - min_value) / (len(nums) - 2)


################### Another Answer ########################
# def centered_average(nums):
#     sum = 0
#     max_value = nums[0]
#     min_value = nums[0]

#     for i in range(len(nums)):
#         sum = sum + nums[i]
#         if nums[i] > max_value:
#             max_value = nums[i]
#         if nums[i] < min_value:
#             min_value = nums[i]

#     return (sum - max_value - min_value) / (len(nums) - 2)

print(centered_average([1, 2, 3, 4, 100]))  # → 3
print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # → 5
print(centered_average([-10, -4, -2, -4, -2, 0]))  # → -3

