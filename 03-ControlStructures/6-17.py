time_24 = input("Enter time (24-hour format): ")
hours, minutes = map(int, time_24.split(':'))

if hours == 0:
    period = 'am'
    hours_12 = 12
elif hours < 12:
    period = 'am'
    hours_12 = hours
elif hours == 12:
    period = 'pm'
    hours_12 = 12
else:
    period = 'pm'
    hours_12 = hours - 12

print(f"Time in 12-hour format: {hours_12}:{minutes:02d}{period}")
