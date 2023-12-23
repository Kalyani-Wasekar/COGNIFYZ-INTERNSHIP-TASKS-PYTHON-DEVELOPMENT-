import re
def valid_email(email):
    # Regular expression for a basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match() to check if the email matches the pattern
    match = re.match(pattern, email)
    
    # Return True if there is a match, indicating a valid email
    return bool(match)

#Get the input from user
email_to_check = input("Enter an email address to validate: ")

if valid_email(email_to_check):
    print(f"{email_to_check} is a valid email address.")
else:
    print(f"{email_to_check} is not a valid email address.")
