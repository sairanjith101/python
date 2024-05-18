def check_digit_sum_balance(number):
    # Convert the number to a string for easier digit extraction
    num_str = str(number)
    
    # Initialize sums for odd and even digits
    odd_sum = 0
    even_sum = 0
    
    # Iterate through the digits
    for i in range(len(num_str)):
        # Convert the digit back to an integer
        digit = int(num_str[i])
        
        # Check if the position is odd or even
        if i % 2 == 0:  # Odd position
            odd_sum += digit
        else:  # Even position
            even_sum += digit
    
    # Check if the difference is zero
    if odd_sum - even_sum == 0:
        return "Yes"
    else:
        return "No"

# Test cases
print(check_digit_sum_balance(1212112))  # Output: Yes
print(check_digit_sum_balance(12345))    # Output: No
