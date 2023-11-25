# 6.	Nested Exception Handling: Handle exceptions within nested try-except blocks and demonstrate the order of execution.



try:
    print("Outer try block")
    
    try:
        print("Inner try block")
        result = 10 / 0  
    except ZeroDivisionError:
        print("Inner except block: ZeroDivisionError")
    finally:
        print("Inner finally block")
    
    result = 10 / 0  
except ZeroDivisionError:
    print("Outer except block: ZeroDivisionError")

