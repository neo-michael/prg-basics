def f(product_code):
    digits = [int(d) for d in product_code[:-1]]
    control_digit = int(product_code[-1])
    return sum(digits) % 7 == control_digit
