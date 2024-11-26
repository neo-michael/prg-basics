import csv

with open("clothing.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    for row in reader:
        if float(row[5]) < 60 and int(row[6]) < 40:
            print(row)