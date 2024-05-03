rno = []
mks = []
for a in range(2):
    r,m=eval(input("Enter the roll no. and marks"))
    rno.append(r)
    mks.append(m)
d={rno[0]:mks[0],rno[1]:mks[1]}
print("Created Dictinary")
print(d)
print("To modify marks")
r=int(input("Enter the roll no:"))
if r in d:
    d[r]=int(input("Enter the marks:"))
else:
    print("No such roll no. found")
print("Modified dictionary:")
print(d)
    
    
