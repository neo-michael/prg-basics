import json

# Open the JSON file in read mode
with open('cities.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)

# Print the JSON data
for city in data:
   for ... , ... in city. ...():
      print(key,':',value)
   print()