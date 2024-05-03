#Sum of series 1+1+2+3+5..... to n
defsumseries2(n):
    sum=0
    term1=1
    term2=1
    term3=0
    count=0
    while count<n:
        term3=term1+term2
        sum+=term3
        term1=term2
        term2=term3
        count+=1
    return sum
5
