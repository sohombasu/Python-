
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)    
print(li)
for i in li:
    if i<0:
       print("Print Negative Numbers",i, end = " ")
