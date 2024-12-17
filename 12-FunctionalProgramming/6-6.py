data = [
    ("Smith", "Lucy"),
    ("Jones", "Janet"),
    ("Lee", "Jerry"),
    ("Jackson", "Peter"),
    ("Johnson", "Rick"),
    ("Lewis", "Terry"),
    ("Clarke", "Robin"),
]

print('\n'.join(map(lambda name: f"{name[0].upper()}, {name[1]}", data)))