# 4.	Division Drill: Take two numbers as input and perform division. Print both the quotient and the remainder.

dividend = float(input("enter the number"))
divisor =float(input("enter the number"))

if divisor == 0:
    print("division by zero is not allowed guys.")
else:
    quotient = dividend / divisor
    remainder = dividend % divisor

    print(quotient)
    print(dividend)