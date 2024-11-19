###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'


# Linux is just better :)
# read the content of email
with open(email_file, 'r', encoding="utf-8") as file:
    email_content = file.read()



# regular expression pattern
# for amounts
pattern = r"€(\d+)"

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email_content)

# calculate the total purchases
print(sum([int(a) for a in amounts]))   