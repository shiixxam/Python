# 9.	Password Strength Checker: Ask the user to create a password. Check if the password is at least 8 characters long and contains at least one uppercase letter using comparison operators and logical AND. Print whether it's a strong password.




password = input("Create a password: ")


if len(password) >= 8 and any(char.isupper() for char in password):
    print("It's a strong password.")
else:
    print("It's not a strong password. Please make it at least 8 characters long and include at least one uppercase letter.")
