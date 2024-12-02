categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

print(sorted(zip(categories, expenses), key=lambda ele: ele[1], reverse=True)[0][0])