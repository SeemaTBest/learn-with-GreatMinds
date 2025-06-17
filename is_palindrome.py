
# Function to check if a given string is a palindrome (case-insensitive)
def is_palindrome(s):
    # Convert the input string to lowercase to make comparison case-insensitive
    s = s.lower()
    
    # Compare the string with its reverse using slicing
    return s == s[::-1]

# Test cases
print(is_palindrome("madam"))     # True - same forward and backward
print(is_palindrome("RaceCar"))   # True - case-insensitive check
print(is_palindrome("Madam"))     # True - case-insensitive check

    