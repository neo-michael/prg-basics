with open("files.txt", 'r') as source:
    contents = source.read().splitlines()

for i in range((len(contents) // 3) + 1):
    with open(f"files.txt.part{i + 1}", 'w') as part:
        for j in range(0, 3):
            index = i * 3 + j
            if index >= len(contents):
                break
            
            part.write(f"{contents[index]}\n")