print("Enter the number of any 5 subjects and calculate its division,percentage,and total marks")
English=int(input())
PE=int(input())
Geography=int(input())
IP=int(input())
Maths=int(input())
average=((English+PE+Geography+IP+Maths)/500)*100
if(average>=60):
    print("First Divison",average)
elif(average<60 and average>=45):
    print("Second Divison",average)
elif(average<45 and average>=33):
    print("Third Divison",average)
elif(average<33):
    print("Fail",average)



