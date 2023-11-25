# 6.	Unpacking Arguments: Call a function by unpacking a list or tuple as its arguments.





def fun(a,b,c):
    return f"Below are the tuples {a}{b}{c}" 
    
    
x=1,2,3
y=fun(*x)
print(y)