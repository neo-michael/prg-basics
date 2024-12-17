import statistics

class Statistics:
    def __init__(self):
        self.data = []
    
    def add(self, n):
        self.data.append(n)
    
    def display(self):
        for n in self.data:
            print(n, end=' ')
        print()
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def avg(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        return statistics.median(self.data)

import random

data = [random.randint(0, 10000) for x in range(10000)]
st = Statistics()
for d in data:
    st.add(d)
st.display()
print(st.max())
print(st.min())
print(st.median())
print(st.avg())