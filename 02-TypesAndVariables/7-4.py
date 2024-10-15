import math

circumference = int(input("Enter tree circumference in cm: "))
diameter = circumference / math.pi
print(f"Tree can be cut down: {diameter >= 50}")