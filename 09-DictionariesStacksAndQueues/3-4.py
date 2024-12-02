import queue

stack = queue.LifoQueue()

number = 18

while not number == 0:
    stack.put(number % 2)
    number //= 2

while not stack.empty():
    print(stack.get(), end='')