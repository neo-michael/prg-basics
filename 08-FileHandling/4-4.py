with open("it_company.csv", 'r') as file:
    i = 0
    while True:
        if i < 5:
            line = file.readline()[:-1]
            if not len(line) == 0:
                print(line)
            else:
                break
            i += 1
        else:
            input("Press Enter key...")
            i = 0
