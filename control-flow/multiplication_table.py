# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
print(f"\nMultiplication table for {number}:\n") # Add a title for the table
for i in range(1, 11): # Loop from 1 to 10 (inclusive)
    product = number * i
    # Print each line of the multiplication table
    print(f"{number} * {i} = {product}")