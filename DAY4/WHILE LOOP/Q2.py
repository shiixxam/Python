# 2.	Password Validation: Ask the user to enter a password. Use a while loop to check if the password meets certain criteria (e.g., length, containing both letters and numbers).

password=input("enter the password:")
password_length = 8

while  len(password) >=password_length and any(char.isalpha() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password)and any(char in '!@#$%^&*()_-+=<>?/' for char in password):
        print("password is successfull genrated")
        break
else:
        print("password is invalid!.  It must be at least  characters long and contain both letters and numbers and spec.".format(password_length)) 









