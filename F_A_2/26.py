import re

def validate_password(password):
    # Validate length
    if len(password) < 6 or len(password) > 16:
        return False

    # Validate lowercase, uppercase, numbers, and special characters
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    
    return True

# Test the function
password = input("Enter the password to validate: ")
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")
