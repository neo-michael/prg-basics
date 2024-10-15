###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

C = float(input("Enter temp in C: "))
K = C + 273.15
F = (C * 9.0 / 5.0) + 32

print(f"The temp in C is: {C}")
print(f"The temp in K is: {K}")
print(f"The temp in F is: {F}")