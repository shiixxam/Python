# 5.	Early Return: Use a return statement to exit a function early if a certain condition is met.



def fun(n):
    if n>=0:
        return True, "you have entered non negative number"
        
    return False, "You have entered negative number. Please enter number again"
     
    
x=fun(9)
print (x)