correct_pin = "0805"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter your PIN code: ")
    if entered_pin == correct_pin:
        print("Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")

if attempts == max_attempts:
    print("Your card is blocked.")
