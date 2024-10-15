# Program to calculate parking fee based on the number of hours parked

hours_parked = float(input('Enter the number of hours parked: '))

if 1 <= hours_parked <= 2:
    fee = 5
elif 3 <= hours_parked <= 6:
    fee = 15
elif hours_parked > 6:
    fee = 20
else:
    fee = 0

print(f'The parking fee is: {fee} PLN')
