
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input("Enter the number of leading prime numbers to find: "))

count = 0 
num = 2 

print("Prime numbers:", end=' ')

while count < N:
    if is_prime(num):
        print(num, end=' ')
        count += 1
    num += 1 
