# F = 9/5 * C + 32

# print("Celsius | Fahrenheit")

for c in range(0, 21):
    print(c, ' ', end="")   # Prints the temperature in Celsius
    f = 9 / 5 * c + 32      # Assigns f to calculate the equivalent temperature in Fahrenheit
    print(round(f, 2))                # Prints the temperature in Fahrenheit