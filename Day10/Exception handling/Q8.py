# 8.	Raising Exceptions: Raise a built-in exception (e.g., ValueError) and handle it using try-except.


try:
    raise ValueError("this is custom valueerror message:")
except Exception as ve:
    print(f"caught a valueerror {ve}")
print("This line is executed after the try-except block.")
