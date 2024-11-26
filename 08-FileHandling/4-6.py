import re
with open("email.txt") as file:
    contents = file.read()

newline_pattern = r"\n"
print(len(re.findall(newline_pattern, contents)))
print(len(contents))
word_pattern = r"\b[^\d\W]+\b"
print(len(re.findall(word_pattern, contents)))