records = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

print(
    "Cities with positive temperatures:",
    ', '.join(list(filter(lambda x: records[x] > 0, records)))
)