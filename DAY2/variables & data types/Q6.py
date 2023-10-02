# 6.	Type Conversion (str to int): Get a numeric string from the user and convert it into an integer. Print the integer value.

a=("10")
b=int(a)
print(b)
print(type(b))






# Get a numeric string input from the user
numeric_string = input("Enter a numeric string: ")

# Convert the numeric string to an integer
try:
    numeric_int = int(numeric_string)
    print("The integer value:", numeric_int)
    print(type(numeric_int))
except ValueError:
    print("Invalid input. Please enter a valid numeric string.")
