# 8.	Password Generator: Ask the user for the length of a desired password and generate a random password with that length, including letters, numbers, and symbols. Display the generated password.








import random
import string

# Ask the user for the desired password length
password_length = input("Enter the desired password length: ")

if password_length.isdigit():
    password_length = int(password_length)
    if password_length <= 0:
        print("Please enter a positive integer.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        print("Generated Password:", password)
else:
    print("Invalid input. Please enter a valid positive integer.")







#DO google to understand this code
