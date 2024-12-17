capacity = 500
tolerance = (capacity * (1 - 0.02), capacity * (1 + 0.02))
bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509,2]

correctly_filled = list(filter(lambda bottle: bottle >= tolerance[0] and bottle <= tolerance[1], bottles))
incorrectly_filled_percent = (1 - (len(correctly_filled) / len(bottles))) * 100
print(int(incorrectly_filled_percent * 100) / 100)