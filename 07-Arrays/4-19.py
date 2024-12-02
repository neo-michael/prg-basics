from collections import Counter

tup = (50, 20, 40, 50, 30, 50)

c = Counter(tup)

print(f"Value: {c.most_common()[0][0]}")
print(f"# of occurences: {c.most_common()[0][1]}")
