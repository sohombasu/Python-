def convert_temperatures(values, from_scale='C', to_scale='F'):
    if from_scale.upper() == 'C' and to_scale.upper() == 'F':
        return [(value, (value * 9/5) + 32) for value in values]
    elif from_scale.upper() == 'F' and to_scale.upper() == 'C':
        return [(value, (value - 32) * 5/9) for value in values]
    else:
        return "Invalid scales"

temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = convert_temperatures(temperatures_celsius)
print("Celsius and Fahrenheit:", temperatures_fahrenheit)
