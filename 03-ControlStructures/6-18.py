x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Point P(0, 0) is at the origin of the coordinate system.")
elif x == 0:
    print("Point P({}, {}) is on the y-axis.".format(x, y))
elif y == 0:
    print("Point P({}, {}) is on the x-axis.".format(x, y))
elif x > 0 and y > 0:
    print("Point P({}, {}) is in the first quadrant of the coordinate system.".format(x, y))
elif x < 0 and y > 0:
    print("Point P({}, {}) is in the second quadrant of the coordinate system.".format(x, y))
elif x < 0 and y < 0:
    print("Point P({}, {}) is in the third quadrant of the coordinate system.".format(x, y))
else:
    print("Point P({}, {}) is in the fourth quadrant of the coordinate system.".format(x, y))
