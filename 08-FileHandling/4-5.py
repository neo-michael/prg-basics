import re

def email_sender(email):
    pattern = r"From:.*<([A-z.]+@[A-z.]+)>"
    return re.search(pattern, email).group(1)

def email_recipient(email):
    pattern = r"To:.*<([A-z.]+@[A-z.]+)>"
    return re.search(pattern, email).group(1)

def email_subject(email):
    pattern = r"Subject:\s(.*)"
    return re.search(pattern, email).group(1)

def email_body(email):
    pattern = r"\n\n([\w\s.,?!@\d+]*)"
    return re.search(pattern, email).group(1)

with open("email.txt", 'r') as file:
    email = file.read()


print(email_sender(email))
print(email_recipient(email))
print(email_subject(email))
print(email_body(email))