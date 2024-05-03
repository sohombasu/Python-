#sort in ascending order
L=[]
print('Enter 10 numbers into a list ', end='\n')
for i in range(0,int(10)):
    inp=int(input())
    L.append(inp)
print('The original (single dimensional array (list)  contains ::')
print(L)
L.sort(reverse=False)
print('The sorted (list)  contains ::')
print(L)


