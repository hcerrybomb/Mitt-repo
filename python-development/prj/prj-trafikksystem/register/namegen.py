import names
import time
import csv
import sys

current_dir = sys.path[0]


nameCount = 0
amt = 100000
namesList = []
start = time.time()
for i in range(amt):
    nameCount = nameCount + 1
    namesList.append(names.get_full_name())
    print(f"\rAdding names to namesList {nameCount}/{amt} time:{round(time.time() - start,2)}s",end=' ')
print("\n\nlist made, elapsed time:",round(time.time() - start,2),"s")

with open('C:\\Users\\wista002\\Mitt-repo\\Mitt-repo\\python-development\\prj\\prj-trafikksystem\\register\\names.csv', 'w',encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name"])
    for item in namesList:
        writer.writerow([item])
print("\n\npushed to csv, elapsed time:",round(time.time() - start,2),"s")