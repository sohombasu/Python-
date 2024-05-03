print("Write a program to convert all these strings to uppercase")
a = []
print("Enter 5 strings into a list")
for i in range(1,6):
    inp=(input())
    a.append(inp)
print("Lowercase Strings =", a)
for i in range(1,6):
    b = [i.upper()for i in a]
print("Uppercase Strings =", b)    
