# 1.	Integer Operations: Write a program that performs addition, subtraction, multiplication, and division on two integer numbers.


while True:
  
  num1 = int(input("enter your number :"))
  operator = input("Enter the operator (+ - * /)")
  num2 = int(input("enter your second nuber :"))
  if num1!=int(num1):
    print("enter valid inetger")
  elif num2!=int(num2):
    print("enter the valid integer:")
    continue

  
    
  
  elif operator == "+":
    print(num1+num2)
  elif operator == "-":
    print(num1-num2)
  elif operator == "*":
    print(num1*num2)
  elif operator == "/":
    print(num1/num2)
    
  
else:
    print(f"{operator} is not a valid operator")
    


# using function method :

#1

def add (x,y):
    return x + y
def subtraction (x,y):
    return x - y
def multiply (x,y):
    return x * y 
def divide (x,y):
   if y == 0:
      print("cannot divide by zero")
      return x / y
   num1=int(input("enter your 1st number :"))
   operator =input("select the operator(+ - * /)")
   num2=int(input("enter your 2nd number :"))
   if num1!=int:
        print("enter the valid integer :")
   elif num2!=int:
        print("enter the valid inetger :")
   elif operator == "+":
        print(f"{num1}+{num2} ={add(num1,num2)}")
   elif operator == "-":
        print(f"{num1}-{num2} ={subtraction(num1,num2)}")
   elif operator == "-":
         print(f"{num1}*{num2} ={multiply(num1,num2)}")
   elif operator == "*":
         print(f"{num1}*{num2} ={multiply(num1,num2)}")
   elif operator == "/":
        print(f"{num1}/{num2} ={divide(num1,num2)}")
   else:
        print(f"{operator} is not a valid operator")

   
        
#2



def add (x,y):
    return x + y
def subtraction (x,y):
    return x - y
def multiply (x,y):
    return x * y 
def divide (x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        return "cannot divide by zero"
    return result
    
while True:
    num1=(input("enter your 1st number :"))
    operator =input("select the operator(+ - * /)")
    num2=(input("enter your 2nd number :"))
    try:
        num1=int(num1)
        num2=int(num2)
    except ValueError:
        print("Enter valid input")
        continue
    break

if operator == "+":
        print(f"{num1}+{num2} ={add(num1,num2)}")
elif operator == "-":
        print(f"{num1}-{num2} ={subtraction(num1,num2)}")
elif operator == "-":
         print(f"{num1}*{num2} ={multiply(num1,num2)}")
elif operator == "*":
         print(f"{num1}*{num2} ={multiply(num1,num2)}")
elif operator == "/":
        print(f"{num1}/{num2} ={divide(num1,num2)}")
else:
        print(f"{operator} is not a valid operator")

           
