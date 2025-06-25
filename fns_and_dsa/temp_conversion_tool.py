FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


while True:
    value = input("Enter the temperature to convert: ")
    if value.lstrip('-').isdigit():
        temperature = int(value)
        break
    else:
        print("Invalid input. Please enter a numeric value.")

tenp_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius():
    conversion_to_celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return conversion_to_celsius

def convert_to_farenheit():
    conversion_to_farenheit = temperature * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return conversion_to_farenheit

if tenp_scale == "C":
    print(f"{temperature}°C is {convert_to_farenheit()}°F")

elif tenp_scale == "F":
    print(f"{temperature}°F is {convert_to_celsius()}°C")