def sum_of_digits(number):
    number = abs(number)
    digits = str(number)
    total = 0
    for digit in digits:
        total += int(digit)
    return total

number = int(input("Enter an integer: "))
result = sum_of_digits(number)
print('The sum of the digits is', result)
