#area of several circles
print('How many cirlces?')
n=int(input())
pi=3.14
for i in range(2,4):
    print('Enter radius')
    radius=float(input())
    area=pi*radius**2
    print('Area =',area)
