import csv

with open("it_company.csv") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if row[2] == "Graphic Designer":
            print(row[1], ' ', row[0], ',', row[3], sep='')
