def f(number, even):
    return sum(int(digit) for digit in str(number) if (int(digit) % 2 == 0) == even)
