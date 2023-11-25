# 1.	Custom Exception Definition: Define a custom exception class (e.g., InvalidInputError).

class CustomError(Exception):
    def __init__(self,msg):
        super().__init__(f"Division by zero is not allowed:{msg}")


def divide(a, b):
    if b == 0:
        raise CustomError(b)
    return a / b

try:
    result = divide(10, 0)
except CustomError as e:
    print("Oops! We got a custom warning:", e)
else:
    print("Division result:", result)
   
   
   
   
   