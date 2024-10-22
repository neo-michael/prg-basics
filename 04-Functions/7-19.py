def f(number):
    digit_count = {}
    for digit in str(number):
        digit_count[digit] = digit_count.get(digit, 0) + 1
    return sum(int(digit) * count for digit, count in digit_count.items() if count > 1)
