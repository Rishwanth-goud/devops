def check_palindrome(input_string):
    # Convert the input string to lowercase to handle case insensitivity
    input_string = input_string.lower()
    
    # Reverse the string and compare with the original string
    reversed_string = input_string[::-1]
    
    # Check if the string is a palindrome
    if input_string == reversed_string:
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')

# Example usage with the string "racecar"
check_palindrome("racecar")

