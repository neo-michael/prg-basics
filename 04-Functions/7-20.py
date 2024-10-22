def f(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count, current = 0, 1
    while count < n:
        current += 1
        if is_prime(current):
            count += 1
    return current
