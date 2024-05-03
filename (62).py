# Report number of occurrences of a number in the list
import random
lst = []
for k in range(20):
   n = random.randint(0, 50)
   lst.append(n)
print(lst)

num =int(input("Enter number : "))
count = 0 
for i in range(len(lst)) :
    if lst[i]== num:
        print("Number found at position:", i)

