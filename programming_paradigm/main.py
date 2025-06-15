import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to parse command-line arguments and call the safe_divide function.
    """
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1) # Exit if the usage is incorrect

    # Get the numerator and denominator from the command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the division function and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()