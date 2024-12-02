monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

food_total = sum(week[0] for week in monthly_expenses)
transport_total = sum(week[1] for week in monthly_expenses)
utilities_total = sum(week[2] for week in monthly_expenses)

week1_total = sum(monthly_expenses[0])
week2_total = sum(monthly_expenses[1])
week3_total = sum(monthly_expenses[2])
week4_total = sum(monthly_expenses[3])

total_expenses = food_total + transport_total + utilities_total

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week1_total)
print('Week 2:', week2_total)
print('Week 3:', week3_total)
print('Week 4:', week4_total)
print('---------------')
print('TOTAL:', total_expenses)
