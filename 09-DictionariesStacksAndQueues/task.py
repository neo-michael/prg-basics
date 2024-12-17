from queue import LifoQueue

# def infix_to_postfix(expr):
#     prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

#     stack = LifoQueue()
#     output = []

#     for char in expr:
#         if char.isalnum():
#             output.append(char)
#         elif char == '(':
#             stack.put(char)
#         elif char == ')':
#             while not stack.empty() and not stack.queue[-1] == '(':
#                 output.append(stack.get())
#             stack.get()
#         elif char in "+-*/^":
#             while not stack.empty() and not stack.queue[-1] == '(' and prec[char] <= prec[stack.queue[-1]]:
#                 output.append(stack.get())
#             stack.put(char)
    
#     while not stack.empty():
#         output.append(stack.get())

#     return ''.join(output)

# print(infix_to_postfix("a+b*c"))



def next_greater(arr):
    stack = LifoQueue()
    output = []

    for i, ele in enumerate(arr):
        for j, next_ele in enumerate(arr[i + 1:]):
            if next_ele > ele:
                output.append(next_ele)
                break
    for i in range(len(arr) - len(output)):
        output.append(-1)
    return output

print(next_greater(next_greater(next_greater([4, 5, 2, 25]))))