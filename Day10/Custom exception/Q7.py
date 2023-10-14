# 7.	Custom Exception in Functions: Create a function that raises a custom exception based on certain conditions.





def divide_numbers(a, b):
    if b == 0:
        raise Exception("Division by zero is not allowed")
    elif a % b == 0:
        raise Exception("Result is a multiple of the divisor")
    return a / b

try:
    result = divide_numbers(10, 0) 
except Exception as e:
    print("Custom Exception:", e)

try:
    result = divide_numbers(12, 6)  
except Exception as e:
    print("Custom Exception:", e)

try:
    result = divide_numbers(15, 3)  
    print("Result:", result)
except Exception as e:
    print("Custom Exception:", e)
