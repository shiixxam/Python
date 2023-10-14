# 5.	Function Reusability: Write a function to calculate the factorial of a number and call it multiple times.

def factorial():
    a=int(input("enter the number"))
    n=1
    for i in range(1,a+1):
        n*=i
        print(n)
factorial()
