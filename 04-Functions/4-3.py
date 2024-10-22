import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

area = triangle_area(a, b, c)
print('The area of the triangle is', area)

# Example dimensions
example_area = triangle_area(3, 4, 5)
print('The area of the triangle with sides 3, 4, and 5 is', example_area)
