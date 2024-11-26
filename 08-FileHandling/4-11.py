with open("powers.txt", 'w') as file:
    for i in range(1, 100 + 1):
        file.write(f"{i},{i**2},{i**3}\n")