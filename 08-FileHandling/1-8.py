with open("pets.txt", 'r') as file:
    contents = file.read()

print(len(contents.split(' ')))