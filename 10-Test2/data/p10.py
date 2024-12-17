def f(array):
    smallest_ele, smallest_ele_x, smallest_ele_y = 9999999999999, 0, 0

    for y, row in enumerate(array):
        for x, ele, in enumerate(row):
            if ele < smallest_ele:
                smallest_ele, smallest_ele_x, smallest_ele_y = ele, x, y
    return smallest_ele_x == smallest_ele_y


print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))