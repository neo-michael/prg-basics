###
# Prints employees employed in a specified position.
#

# Employee List
file_name = "it_company.csv"

# Position
job_title = "Software Engineer"

with open(file_name) as file:
    i = 1
    for line in file:
        if job_title in line:
            print(f"{i}. {line[:-1]}")
            i += 1
        
