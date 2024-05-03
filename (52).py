#Sum of numbers divisible by 3 and 5 from an array List
L=[]
print('Enter 10 number into a list ', end='\n')
for i in range(0,int(10)):
    inp=int(input())
    L.append(inp)
print('The original (single dimensional array (list)  contains ::')
print(L)
sum=0
#Finding sum
for i in range(0,int(10)):
    if L[i] % 3==0 or L[i]%5 ==0:
        sum+=L[i]
print('Sum of numbers divisible by 3 or 5 are ::', sum)

