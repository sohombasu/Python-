#finding the second smallest number
import math
print('Enter three unequal numbers')
a=input()
b=input()
c=input()
fmi=(a<b)and a or b
fmx=(a>b)and a or b
smi=(fmx<c)and fmx or c
print('Second smallest is ::',smi)


