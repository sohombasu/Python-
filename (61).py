print("Creating two lists,one containing positive numbers and another containing negative numbers")
a = []
print("Enter 10 numbers into a list")
for i in range(0,int(10)):
    inp=int(input())
    a.append(inp)
print(a)
a1 = []
a2 = []
for i in a:
    if i < 0:
        a1.append(i)
    else:
        a2.append(i)
print("The list with positive elements:",a1)
print("The list with positive elements:",a2)
