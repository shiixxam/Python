# 7.	Factorial Calculation: Calculate and print the factorial of a number entered by the user using a for loop.




number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")
