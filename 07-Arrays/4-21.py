arr = [2.5, 3.7, 1.2, 6.8, 4.1, 5.9]
value = float(input("Enter a value: "))

count = sum(1 for x in arr if x > value)

print("Number of elements greater than", value, ":", count)
