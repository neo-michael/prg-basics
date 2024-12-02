def compare(a1, a2):
    if not len(a1) == len(a2):
        return False

    for ele in zip(a1, a2):
        if not ele[0] == ele[1]:
            return False
    return True


print(compare(["water", "book", "sky"], ["water", "book", "sky"]))
print(compare([True, False], [True, False, True]))
print(compare([5, 3, 1], [5, 3, 1]))
print(compare([3, 2, 1], [3, 2]))
