arr = [34, 7, 19, 4, 21, 8]

c = 0
i = 0
while i < len(arr):
    if arr[i] & 1 == 0:
        c += 1
    i += 1
print(c)