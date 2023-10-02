# 5.	Calculator Menu: Develop a simple calculator program that offers a menu with options for addition, subtraction, multiplication, and division. Prompt the user to choose an operation and input numbers accordingly. Display the result.


print("Calculator Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if choice == '1':
    print (num1 + num2)
    operation = "Addition"
elif choice == '2':
    print(num1 - num2)
    operation = "Subtraction"
elif choice == '3':
    print(num1 * num2)
    operation = "Multiplication"
elif choice == '4':
    if num2 == 0:
        print( "Division by zero is not allowed.")
    else:
        print( num1 / num2)
    
else:
    print("Invalid choice")
   


