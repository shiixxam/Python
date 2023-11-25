# 9.	Zero Division Error Handling: Write a program that takes two numbers as input and handles the zero division exception using a try-except block.



try:
    num1=float(input("enter the number"))
    num2=float(input("enter the number"))
    result=num1/num2
    print(f"Results: {result}")


except ZeroDivisionError as ze:
    print(f"number can not be divide by zero ")
