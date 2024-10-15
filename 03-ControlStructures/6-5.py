# Program that simulates the operation of an electronic thermometer.

temperature = 32

if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
else:
    print("Warning, frost")

test_temperatures = [33, 30, 8, 0, -2]
for temp in test_temperatures:
    print(f'Temperature: {temp}°C - ', end='')
    if temp > 35:
        print("It is extremely hot")
    elif temp > 30:
        print("It is hot")
    elif temp >= 15:
        print("It is warm")
    elif temp >= 0:
        print("It is cold")
    else:
        print("Warning, frost")
