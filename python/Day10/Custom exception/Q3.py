# 3.	Custom Exception Handling: Handle the custom exception using try-except and print a custom error message.


class customerror(Exception):
    def __init__(self,message ):
        self.messgae= message
        super().__init__(self.messgae)


def divide(a,b):
    if b==0:
        raise customerror("Division by zero is not allowed")
    return a/b
try:
    a=float(input("enter the number : "))
    b=float(input("enter the number : "))
    print(a/b)
    
except customerror as e:
    print(f"custom error: {e}")
