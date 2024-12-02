from queue import LifoQueue

def is_digit(c):
    return c in "1234567890"
def is_operator(c):
    return c in "+-/*"

def eval_rpn(expr):
    stack = LifoQueue()
    for c in expr:
        if is_digit(c):
            stack.put(c)
        if is_operator(c):
            right = stack.get()
            left = stack.get()
            stack.put(eval(f"{left}{c}{right}"))
        if c == '=':
            print(stack.get())
            break
eval_rpn("831+/32-4+*=")