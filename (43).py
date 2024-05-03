yr = int(input("Enter 4 digit:"))
if yr%100==0:
    if yr%400==0:
        print(yr,"Its a leap Year")
elif yr%4==0:
    print(yr,"Its a leap year")

else:
    print(yr,"Its not a Leap Year")
    
