# 1.	Division Error Handling: Write a program that takes two numbers as input and handles the division by zero exception using a try-except block.

a=int(input("enter the first number:"))
b=int(input("enter the second numbeer:"))


try:

    c=a/b
    print("Result: ",c)
except:
    print("can't divide by zero....!")
else:
    print(a/b)
