celsius = float(input("Ingresa la temperatura en grados Celsius: "))

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} celsius Equivale a: {fahrenheit} fahrenheit")
