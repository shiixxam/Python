# 8.	Number Range Check: Request a number from the user and compare it to a specific range (e.g., 1 to 100) using the greater than, less than, and logical AND operators.
# Print whether the number is within the range.



number = int(input("Enter a number: "))

a=1
b= 100

if number >= a and number <= b:
    print("The number is within the range [1, 100].")
else:
    print("The number is outside the range [1, 100].")
