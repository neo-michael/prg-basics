price = float(input("Enter price: "))
discount = int(input("Enter discount: ")) / 100.0


print(f"Price with discount: {price * (1 - discount):.2f}")
print(f"Reduction: {price * discount:.2f}")