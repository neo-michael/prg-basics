arr = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i, inner_arr in enumerate(arr):
    arr[i][i] = 1
    for ele in inner_arr:
        print(ele, end=" ")
    print()