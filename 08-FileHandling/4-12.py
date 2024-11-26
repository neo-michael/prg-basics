classification = {}

import csv

with open("books.csv", 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        key = row[2].replace(' ', '_').lower()
        if key in classification:
            classification[key].append(','.join(row))
        else:
            classification[key] = [','.join(row)]

for genre in classification:
    with open(f"books/books_{genre}.txt", 'w') as file:
        for book_data in classification[genre]:
            file.write(book_data)
            file.write('\n')