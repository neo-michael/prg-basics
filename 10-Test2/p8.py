from queue import LifoQueue

def f(expression):
    expression = expression.split(' ')
    stack = LifoQueue()

    for char in expression:
        if char.isdigit():
            stack.put(char)
        elif char in "+-":
            right = stack.get()
            left = stack.get()
            result = eval(f"{left}{char}{right}")
            stack.put(result)

    return stack.get()

print(f("2 3 +"))
print(f("2 6 + 4 5 - +"))
print(f("11 7 + 15 - 14 +"))