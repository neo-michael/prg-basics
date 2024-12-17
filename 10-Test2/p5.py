import re


def f(first_letter, last_letter):
    with open("data/data.txt", 'r', encoding="utf-8") as file:
        contents = file.read()
        results = re.findall(fr"\b[{first_letter}{first_letter.upper()}][A-Za-z']*{last_letter}\b", contents)
        return len(results)

print(f('w', 'd'))