#Finding a number using linear search from an array List
L=[]
print('Enter 10 numbers into a list ', end='\n')
for i in range(0,int(10)):
    inp=int(input())
    L.append(inp)
print('The original (single dimensional array (list)  contains ::')
print(L, end='\n')
print('Enter a number to search ', end=' ')
search=int(input())
#Finding a number
posn=-1
for i in range(0,int(10)):
    if L[i]==search:
        posn=i+1
        break
print(search , ' was found in the list at the position :: ', posn)
