# Simple Calculator: Create a basic calculator program that takes two numbers as input and allows the user to choose an operation (addition, subtraction, multiplication, division) to perform. Display the result using print() 




num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))

operators=input("+ - / * ")

if operators == "+":    
    print(round(num1+num2,))

elif operators == "-":
    print(round(num1-num2))

elif operators == "*":
    print(round(num1*num2))

elif operators == "/":
    if num2 == 0:
        print("cannot divide by zero")

    else:
        print(num1/num2)

else:
    print("enter the valid numbers")
   
