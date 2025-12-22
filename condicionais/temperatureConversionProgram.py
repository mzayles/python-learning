""" Python - Bro Code """

unit = input("Is this temperature is in Celsius or Fahrenheit? (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    print(f"\nFahrenheit: {(9 * temp / 5) + 32:,.1f}°F")
elif unit == "F":
    print(f"\nCelsius: {temp - 32 * (5 / 9):,.1f}°C")
else:
    print("\nThis unit is not valid.")