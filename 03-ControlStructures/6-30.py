# Program to print a lottery coupon (numbers from 1 to 49)

# Initialize the maximum number and the number of columns
max_number = 49
columns = 7

# Loop through each row
for row in range(1, 8):  # There will be 7 rows
    # Initialize an empty string for the current row
    current_row = ''
    
    # Loop through each column
    for col in range(columns):
        # Calculate the number to be printed
        number = (col * 7) + row
        current_row += f'{number} '  # Append the number to the current row
    
    # Print the current row, stripping the trailing space
    print(current_row.strip())
