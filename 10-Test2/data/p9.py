import csv

def f(value):
    counter = 0
    with open('data/data.csv', 'r', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for line in reader:
            if int(line[-5]) >= value:
                counter += 1
    return counter
print(f(9200))
print(f(11640))