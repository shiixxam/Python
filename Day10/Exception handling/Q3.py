# 3.	Custom Exception Handling: Create a custom exception class and raise it in your code. Handle the custom exception using try-except.



try:
    number=int(input("enter the number"))
    if number < 0:
        print("number cannot be negative")
    else:
        print("Number is valid")
except Exception as e:
    print(f"an error occured:{e}")
