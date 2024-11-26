import re

pattern = r".*\..{4}"

counter = 0
with open("files.txt", 'r') as file:
    for line in file:
        if re.match(pattern, line):
            counter += 1
print(counter)