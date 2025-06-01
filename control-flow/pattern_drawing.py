# This script draws a square pattern of asterisks based on user input for the size.
try:
    # Prompt User for Pattern Size
    size = int(input("Enter the size of the pattern: "))

    if size <= 0:
        print("Please enter a positive integer for the size.")
    else:
        # Draw the Pattern
        # Outer while loop for rows
        row = 0
        while row < size:
            # Inner for loop for columns (asterisks in a row)
            for _ in range(size):
                print("*", end="") # Print asterisk without a new line
            print() # Move to the next line after printing all asterisks in a row
            row += 1 # Increment row counter

except ValueError:
    # Handle cases where input cannot be converted to an integer
    print("Invalid input. Please enter a whole number for the size.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")