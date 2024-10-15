age = int(input("Enter your age: "))

if age < 13:
    age_group = "Child"
elif 13 <= age <= 19:
    age_group = "Teen"
elif 20 <= age <= 64:
    age_group = "Adult"
else:
    age_group = "Senior"

print(f"You belong to the age group: {age_group}")
