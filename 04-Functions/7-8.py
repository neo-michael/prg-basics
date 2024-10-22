def f(amount_to_pay):
    coins = [5, 2, 1]
    count = 0
    for coin in coins:
        count += amount_to_pay // coin
        amount_to_pay %= coin
    return count



def main():
    amount_to_pay = 11
    print(f(amount_to_pay))

if __name__ == "__main__":
    main()
