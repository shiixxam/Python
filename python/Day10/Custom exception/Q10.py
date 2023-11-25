# 10.	Handling Built-in and Custom Exceptions: Write a program that raises both built-in and custom exceptions and handles them using try-except blocks.


class CustomException(Exception):
    pass

try:
    result = 10 / 0
except ZeroDivisionError as zero_error:
    print("Caught a built-in ZeroDivisionError:", zero_error)

try:
    raise CustomException("This is a custom exception")
except CustomException as custom_error:
    print("Caught a custom exception:", custom_error)
