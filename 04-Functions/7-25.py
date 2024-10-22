def f(x, y):
    return sum(num for num in range(x, y + 1) if num % 2 == 0 and num % 3 == 0 and num % 4 != 0)
