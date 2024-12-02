def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubbleSort([8, 43, 14, 84, 26, 4, 98, 125, 71]))
print(bubbleSort([8, 1, 43, 14, 2, 84, 26, 4, 98, 125, 71]))
print(bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))