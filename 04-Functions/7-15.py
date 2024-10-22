def f(detector):
    count = 0
    for action in detector:
        if action == '+':
            count += 1
        elif action == '-':
            count -= 1
        if count >= 3:
            return True
    return False
