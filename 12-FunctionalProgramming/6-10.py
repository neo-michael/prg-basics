import matplotlib.pyplot as plt

data = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

x = list(map(lambda e: e, data))
y = list(map(lambda e: data[e], data))

plt.bar(x, y)

plt.xlabel("City")
plt.ylabel("Temperature in C")

plt.title("Weather forecast")

plt.show()