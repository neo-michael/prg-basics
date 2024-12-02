arr = [12, 7, 5, 22, 13, 8, 19, 24, 6]

even_numbers = [x for x in arr if x % 2 == 0]
odd_numbers = [x for x in arr if x % 2 != 0]
sorted_arr = even_numbers + odd_numbers

print("Separated array:", sorted_arr)
