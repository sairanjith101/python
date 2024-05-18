def validate_password(password):
    # Validate length
    if len(password) < 6 or len(password) > 16:
        return False
    
    # Initialize flags for each requirement
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    # Check each character in the password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in '$#@':
            has_special = True
    
    # Check if all requirements are met
    if has_lower and has_upper and has_digit and has_special:
        return True
    else:
        return False

# Test the function
password = input("Enter the password to validate: ")
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")
