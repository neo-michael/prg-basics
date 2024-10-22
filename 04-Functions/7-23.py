def f(password):
    return len(password) >= 6 and len(password) == len(set(password))
