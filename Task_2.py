# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

filename = 'text_2_var_59'
with open(filename) as file:
    lines = file.readlines()

avg_lines = list()

for line in lines:
    # print (line.strip())
    nums = line.split(',')
    # print(nums)
    sum_line = 0

    for num in nums:
        sum_line += int(num)

    if len(nums) > 0:
        avg_lines.append(sum_line / len(nums))


with open('results_text_2.txt', 'w') as result:
    for value in avg_lines:
        result.write(str(value) + "\n")

