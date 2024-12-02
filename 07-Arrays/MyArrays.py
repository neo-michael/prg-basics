import statistics

def second_largest(arr):
    return sorted(arr)[-2]

def min_max_diff(arr):
    return max(arr) - min(arr)


def median2(arr):
    return sroted(arr)[len(arr) // 2] if n % 2 == 1 else (arr[(n // 2) - 1] + arr[n // 2]) / 2

def median(arr):
    arr = sorted(arr)
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        i = n // 2
        return (arr[i - 1] + arr[i]) / 2

def min_max(arr):
    return (min(arr), max(arr))

def print_arr(arr):
    return '-'.join((str(ele) for ele in arr))