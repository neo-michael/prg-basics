import queue

def reverse(string):
    stack = queue.LifoQueue()
    for c in string:
        stack.put(c)
    
    rev = ""
    while not stack.empty():
        rev += stack.get()

    return rev
print(reverse("Push each character of the string onto the stack, then pop characters to form the reversed string."))