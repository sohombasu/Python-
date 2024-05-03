print("Converts list of temperatures in Fahrenheit degrees to equivalent Celsius degree")
fah = []
print("Enter temperature in fah")
for i in range(0,int(5)):
    inp=int(input())
    fah.append(inp)
print("Farenheit =", fah)
cel = []
for i in fah:
    c = (i - 32) * 5 / 9
    cel.append(c)
print("Celsius = ", cel)    
