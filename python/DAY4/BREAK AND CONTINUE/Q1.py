# 1.	Break Loop: Create a program that asks the user to guess a number and uses a while loop. If the user guesses the correct number, use the break statement to exit the loop.



from random import randint

secret_number=randint(1,10)

print("Welcome to the Guessing Game!")
print("Try to guess it")

while True:
    guess=int(input("guess the number from 1 to 10 :"))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break  
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
        