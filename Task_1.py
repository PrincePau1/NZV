# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

filename = 'text_1_var_59'
with open(filename) as file:
    lines = file.readlines()

word_stat = dict()

for line in lines:
    # print(line.strip())
    row = (line.strip()
           .replace("!", " ")
           .replace("?", " ")
           .replace(".", " ")
           .replace(",", " ")
           .strip())
    # print(row)
    words = row.split(" ")
    # print(words)
    for word in words:
        if word in word_stat:
            word_stat[word] += 1
    else:
            word_stat[word] = 1

# print(word_stat)

word_stat = (dict(sorted(word_stat.items(), reverse=True, key=lambda item: item[1])))
#
# print(word_stat)
#
with open('results_text_1.txt', 'w') as result:
    for key, value in word_stat.items():
        result.write(key + ":" + str(value) + "\n")