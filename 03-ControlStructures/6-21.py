amount = int(input("Enter the amount in PLN: "))

coins_5 = amount // 5
amount %= 5

coins_2 = amount // 2
amount %= 2

coins_1 = amount // 1

print("The amount of PLN {} in coins:".format(amount))
print("5 PLN coins:", coins_5)
print("2 PLN coins:", coins_2)
print("1 PLN coins:", coins_1)
