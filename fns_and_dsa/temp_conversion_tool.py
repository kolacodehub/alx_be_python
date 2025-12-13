FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}°F is {result}°C"


def convert_to_fahrenheit(celcius):
    result = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f"{celcius}°C is {result}°F"


def display_temperature_converter():
    userInput = float(input("Enter the temperature to convert: "))
    operation = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
    if operation == "C":
        print(convert_to_fahrenheit(userInput))
    elif operation == "F":
        print(convert_to_celsius(userInput))
    else:
        print("Invalid option, pick c or f")


display_temperature_converter()
