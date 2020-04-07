# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.

# Answer:
# step 0:
# Declar a sum and intalize it to 0

# Step 1:
# Inspect the first element to see
# if it is 13. We have to do this since in step 2 we will have a loop which
# inspects the element prior to see if it is 13. if we start the loop
# at index 0 the program would try to inspect the element at index -1

# Step 2:
# Loop through list and inspect element to see that it is not 13and the
# previous element is not 13, if list [i] and list[i -1] != 13 add to sum

# Step 3: Retrun sum


# def sum13(nums):
#     sum = 0
#     if len(nums) > 0 and nums[0] != 13:
#         sum = nums[0]

#     for i in range(1, len(nums)):
#         if nums[i] != 13 and nums[i - 1] != 13:
#             sum += nums[i]
#     return sum

########################### Another Answer #######################


def sum13(nums):
    ele_sum = 0
    i = 0

    while i < len(nums):
        if nums[i] != 13:
            ele_sum += nums[i]
        else:
            index += 1  # nums[i] is 13, so skip the next element
        index += 1
    return ele_sum


print(sum13([1, 2, 2, 1]))  # → 6
print(sum13([1, 1]))  # → 2
print(sum13([1, 2, 2, 1, 13]))  # → 6

