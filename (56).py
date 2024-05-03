print("Removing all the duplicates from a list")
a = []
print("Enter 20 numbers into a list")
for i in range(0,int(20)):
    inp=int(input())
    a.append(inp)
print(a)
b = []
for i in a:
    if i not in b:
        b.append(i)
print("The resultant list after removing duplicates is ",b)  

        
