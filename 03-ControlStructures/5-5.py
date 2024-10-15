###
# Sums numbers entered by user
#
total_sum = 0
number = int(input("Enter a number (0 to stop): "))
amount = number
while True:
    if number == 0:
        break  
    total_sum += number
    number -= 1

print(f"The total sum of the numbers is: {total_sum}")
print(f"The avg of the numbers is: {total_sum / amount}")