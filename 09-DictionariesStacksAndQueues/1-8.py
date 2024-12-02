price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print(price_list)

print(sum(price_list.values()))
for key in price_list:
    price_list[key] = round(price_list[key] * 0.9, 2)

print(price_list)
print(sum(price_list.values()))