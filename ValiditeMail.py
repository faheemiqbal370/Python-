import re

def check_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")

email = input("Enter an email: ")
check_email(email)
