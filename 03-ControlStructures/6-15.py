ean_number = input("Enter EAN-13 article number: ")

if len(ean_number) == 13 and ean_number.isdigit():
    print("Article number is correct")
    if ean_number.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Article number is incorrect")
