def f(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    
    return arr[0]

print(f([7,7,7,7,7,7,5,7,7]))
print(f([5,5,5,5,5,5,7,5,5]))
