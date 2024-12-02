import json

# Read the contents of the json file
with open("voting.json", 'r') as file:
    voting = json.load(file)

# Vote for a person
person_name = input('Name of the person you are voting for:')
if person_name in voting:
    voting[person_name] += 1
else:
    voting[person_name] = 1

# Save voting data to json file
with open("voting.json", 'w') as wfile:
    wfile.write(json.dumps(voting, indent=4))