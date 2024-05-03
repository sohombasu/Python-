def ispalindrome(num): 
    copy=num 
    reverse=0 
    while copy>0: 
        digit= copy % 10 
        reverse=(reverse*10)+digit 
        copy//=10 
    if num==reverse: 
        return True 
    else: 
        return False 




