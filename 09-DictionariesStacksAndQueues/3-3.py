import queue

# [(
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct


def brackets_ok(expression):
    stack = queue.LifoQueue()
    for c in expression:
        if c in ['[', '(', '{']:
            stack.put(c)
        elif c in [']', ')', '}']:
            if stack.empty():
                return False
            top = stack.get()
            if (c == ']' and top != '[') or (c == '}' and top != '{') or (c == ')' and top != '('):
                return False
    return stack.empty()

for i, exp in enumerate([expression1, expression2, expression3]):
    if brackets_ok(exp):
        print(f"Expr {i + 1} is ok")
    else:
        print(f"Expr {i + 1} is not ok")
