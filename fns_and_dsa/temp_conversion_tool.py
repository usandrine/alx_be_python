#!/usr/bin/env python3
"""
temp_conversion_tool.py

A script to convert temperatures between Celsius and Fahrenheit, 
illustrating the use of global variables for conversion factors.
"""

# Define Global Conversion Factors
# Factor for converting (Fahrenheit - 32) to Celsius
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
# Factor for converting Celsius to Fahrenheit 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    Parameters:
    - fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
    - float: Temperature in degrees Celsius.
    """
    # Celsius = (Fahrenheit - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    Parameters:
    - celsius (float): Temperature in degrees Celsius.

    Returns:
    - float: Temperature in degrees Fahrenheit.
    """
    # Fahrenheit = (Celsius * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """Handles user interaction for temperature conversion."""
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input) # Attempt to convert to float

        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        # Handle non-numeric temperature input
        raise ValueError("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)