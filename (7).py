countzero=0
print('Enter your number')
for i in range(0,5):
    num=int(input())
    if num%10==5:
        print(num)
    elif num%10==0:
        countzero=countzero+1
print('Number ending with zero', countzero)

    
