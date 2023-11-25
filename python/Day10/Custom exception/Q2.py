# 2.	Custom Exception Raising: Raise the custom exception in your code when a specific condition is met.

#we create negtivenumber error exception

class negativenumbererror(Exception):

    def __init__(self,number):
        super().__init__()


    def postive_number(number):
        if number < 0:
            raise negativenumbererror()
        else:
            print(f"positive number: {number}")

    try:
        user_number=int(input("enter the number"))
        postive_number(user_number)
    except Exception as e:
        print(f"invalid input. please enter the valid number")
   