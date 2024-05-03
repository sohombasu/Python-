# Convert fahrenheit temperatures in list into centigrade 
fahr =[212, 120, 100, 93, 37] 
for i, f in enumerate(fahr):
    c=int(5/9 * (f-32))
    fahr[i] = c
    print(f, c)
    print(fahr)
