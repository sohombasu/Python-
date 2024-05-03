num= [1, 2, 3, 4, 5, 6, 7]
n = len * (num) 
if n%2==0:
  i = int  (n / 2 - 1) 
  j = int  (n / 2)
  median = (num[i] + num[j]) / 2
else:
  i = int  (n / 2)
  median = num[i]
print('Median value=', median)
