# 10.	Recursive Function: Write a recursive function to calculate the nth Fibonacci number.


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

a = int(input("enter number: "))
result = fib(a)
print(f"The {a}th Fibonacci number is: {result}")