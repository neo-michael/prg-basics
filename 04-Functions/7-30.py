def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

def main():
    n = 10
    print(sum_natural(n))

if __name__ == "__main__":
    main()
