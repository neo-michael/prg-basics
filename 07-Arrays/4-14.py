from collections import Counter

arr = [2, 3, 2, 5, 8, 1, 9, 8]


print([key for key, count in Counter(arr).most_common() if count == 1])

