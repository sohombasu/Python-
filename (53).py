#Finding the largest and smallest number from an array List
L=[]
print('Enter 10 numbers into a list ', end='\n')
for i in range(0,int(10)):
    inp=int(input())
    L.append(inp)
print('The original (single dimensional array (list)  contains ::')
print(L, end='\n')
max=min=L[0]
#Finding largest and smallest
for i in range(0,int(10)):
    if L[i]>max:
        max=L[i]
    elif L[i]<min:
        min=L[i]
print('Largest number  ::',max, '\n Smallest number ::', min)
