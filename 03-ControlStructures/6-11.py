current_price = 140.00
previous_price = 200.00

price_reduction = previous_price - current_price
reduction_percentage = (price_reduction / previous_price) * 100

if reduction_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction_percentage:.0f}%")
