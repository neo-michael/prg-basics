import re

data = input("Enter a sentence: ")

pattern = r"[eyioau]"
print(len(re.findall(pattern, data)))