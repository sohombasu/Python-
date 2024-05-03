# Separate positive and negative numbers into two lists
st1=[1,-9,-6,-45,-78,-1,2,3,4,5]
Ist2 = [] 
Ist3 = []
count, ncount =0,0
for num in Ist1:
if num >= 0:
  Ist2.append(num)
else: 
  Ist3.append(num)
print('Original list:', Ist1)
print('Positive numbers list:', Ist2) 
print('Negative numbers list:', Ist3)
