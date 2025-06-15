# explore_datetime.py
# This script demonstrates basic usage of Python's datetime module.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current date and time and prints it in a formatted string.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(start_date):
    """
    Prompts the user for a number of days and calculates the future date.
    
    Args:
        start_date (datetime): The starting date to add days to.
    """
    try:
        # Prompt the user to enter a number of days
        num_days_str = input("Enter the number of days to add to the current date: ")
        
        # Convert the user input string to an integer
        number_of_days = int(num_days_str)
        
        # Calculate the future date by adding the specified number of days
        # timedelta represents a duration
        future_date = start_date + timedelta(days=number_of_days)
        
        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        # Handle cases where the user does not enter a valid integer
        print("Invalid input. Please enter a whole number for the number of days.")

# --- Main execution part of the script ---
if __name__ == "__main__":
    # Part 1: Display the current date and time
    # The function returns the current datetime object which we can use in the next part
    today = display_current_datetime()
    
    print("-" * 20) # Separator for clarity
    
    # Part 2: Calculate a future date
    if today:
        calculate_future_date(today)