import matplotlib.pyplot as plt

medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7},
]


x = list(map(lambda ele: ele["country"], medals))
y = list(
    map(lambda ele: sum(filter(lambda val: str(val).isnumeric(), ele.values())), medals)
)

plt.bar(x, y)

plt.xlabel("City")
plt.ylabel("Medals")

plt.title("Total medals wons")

plt.show()
