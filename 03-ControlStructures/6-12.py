number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

total_price = number_of_products * product_price

if number_of_products > 2:
    total_price *= 0.75  

print(f"Amount to pay: {total_price:.2f}")
