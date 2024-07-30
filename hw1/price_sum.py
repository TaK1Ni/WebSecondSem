import csv
# -*- coding: utf-8 -*-
adult_total, pensioner_total, child_total = 0,0,0

with open('file/products.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        adult_total+=float(row[1])
        pensioner_total+=float(row[2])
        child_total+=float(row[3])
    
print(round(adult_total,2), round(pensioner_total,2), round(child_total,2))