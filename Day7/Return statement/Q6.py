# 6.	Function Composition: Create two functions and call one within the other, returning the result.




def sum(n1,n2,n3):
    add=n1+n2+n3
    return add

def func():
    func=sum("n1,n2,n3")
    return func
     
a=sum(2,3,4)
print ("Average is:", a)