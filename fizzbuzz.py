# Print numbers 1 to n. 
# If divisible by 3, print "Fizz"; 
# If divisible by 5, print "Buzz"; 
# If divisible by both 3 and 5, print "FizzBuzz".

def fizz_buzz(n):
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):

        # Check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print(i, "-> FizzBuzz")

        # Check if the number is divisible by 3 only
        elif i % 3 == 0:
            print(i, "-> Fizz")

        # Check if the number is divisible by 5 only
        elif i % 5 == 0:
            print(i, "-> Buzz")

        # If none of the above, just print the number
        else:
            print(i)

# Call the function with 15 as the upper limit
fizz_buzz(15)

        
            
    