import csv
from collections import Counter

with open("province.csv") as file:
    csvr = csv.DictReader(file)
    province = {row['Letter']:row['Name'] for row in csvr}

with open("vehicle.txt", encoding="utf-8") as f:
    vehicles = f.readlines()
    vehicles_first_letters = [line[0] for line in vehicles]

c = Counter(vehicles_first_letters)
for p in c.most_common():
    print(province[p[0]], p[1])



