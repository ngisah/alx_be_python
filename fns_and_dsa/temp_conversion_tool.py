FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
 
    # This function reads the global variable FAHRENHEIT_TO_CELSIUS_FACTOR.
    # No 'global' keyword is needed because we are only accessing it, not modifying it.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
 
    # This function reads the global variable CELSIUS_TO_FAHRENHEIT_FACTOR.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
   
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Prompt user for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on the unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        # Handle cases where the temperature input is not a valid number
        print("Invalid temperature. Please enter a numeric value.")

# --- Main execution part of the script ---
if __name__ == "__main__":
    main()