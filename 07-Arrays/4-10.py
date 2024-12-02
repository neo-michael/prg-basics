arr = [2, 6, 4, 9, 7]

def star(n):
    return '*' * n

for ele in arr:
    print(f"{ele}: {star(ele)}")