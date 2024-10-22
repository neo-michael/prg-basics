def f(x, y):
    return sum(1 for number in range(x, y + 1) if number < 0 and number % 2 == 0)
