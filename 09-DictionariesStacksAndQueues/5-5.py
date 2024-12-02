from collections import Counter

paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split(' ')
counter = Counter(words)

print(counter.most_common())
