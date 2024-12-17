def f(subjects):
    def avg_g(arr):
        return sum(arr) / len(arr)

    averages = {key: avg_g(value) for key, value in subjects.items()}
    
    return max(averages, key=averages.get)

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))