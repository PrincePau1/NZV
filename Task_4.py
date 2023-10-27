# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv

aver_salary = 0
items = list()

with open('text_4_var_59', newline='\n', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        item = {
            'number': int(row[0]),
            'name': row[2] + ' ' + row[1],
            'age': int(row[3]),
            'salary': int(row[4][0:-1])
        }

        aver_salary += item['salary']
        items.append(item)

aver_salary /= len(items)

filtered = list()
for item in items:
    if (item['salary'] > aver_salary) and item['age'] > 25 + 59 % 10:
        filtered.append(item)

filtered = sorted(filtered, key=lambda i: i['number'])

with open('result_text_4.csv', 'w', encoding="utf-8", newline='') as result:
    writer = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for item in filtered:
        writer.writerow(item.values())