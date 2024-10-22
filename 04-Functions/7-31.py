def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

def main():
    result = power(5, 3)
    print(result)

if __name__ == "__main__":
    main()
