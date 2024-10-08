###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume = a * b * c
surface_area = 2 * a * b + 2 * a * c + 2 * b * c
print(f'The volume of a cube with sides {a}, {b} and {c} is {volume}')
print(f'The surface area of a cube with sides {a}, {b} and {c} is {surface_area}')