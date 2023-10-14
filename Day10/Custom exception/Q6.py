# 6.	Custom Exception with Parameters: Define a custom exception class that accepts parameters and include these parameters in the error message.


value1= "value1"
value2= "value1"

try:
    if not isinstance(value1, int):
        raise f"Custom Exception: param1={value1}, param2={value2}"
except Exception as e:
    print(e)
