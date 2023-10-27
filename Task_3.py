# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

filename = 'text_3_var_59'
with open(filename) as file:
    lines = file.readlines()

matrix = list()

for line in lines:
    nums = line.strip().split(",")
    for i in range(len(nums)):
        if nums[i] == "NA":
            nums[i] = str((int(nums[i - 1]) + int(nums[i + 1])) / 2)

    filtered = list()
    for item in nums:
        num = float(item)
        if math.sqrt(num) > 50 + 59:
            filtered.append(num)

    matrix.append(filtered)

with open('results_text_3.txt', 'w') as result:
    for row in matrix:
        for num in row:
            result.write(str(num) + ',')
        result.write("\n")