# 6.	User Input Validation: Create a program that asks the user to enter a number. Ensure the input is a valid integer. If not, display an error message and ask again until a valid integer is entered.


while True:
    user = input("Enter a number: ")

    if user.isdigit():
        number = int(user)
        print("You entered a valid integer:", number)
        break
    else:
        print("Invalid input. Please enter a valid integer.")
