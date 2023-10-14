# 5.	Custom Exception Inheritance: Create a custom exception class that inherits from a built-in exception class (e.g., ValueError).





class CustomValueError(ValueError):
    pass


try:
    value = int(input("Enter a positive even number: "))
    if value % 2 != 0 or value <= 0:
        raise CustomValueError("Invalid input. Please enter a positive even number.")
except CustomValueError as e:
    print("Custom ValueError:", e)
except ValueError:
    print("ValueError: Invalid input. Please enter an integer.")
