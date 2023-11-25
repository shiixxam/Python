# 1.	Guessing Game: Create a program that asks the user to guess a secret number. Use a while loop to repeatedly ask for guesses until the correct number is guessed.


from random import randint


secret_number=randint(1,10)

attempt=0
guess=None





print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("Try to guess it")


while guess!= secret_number:
    guess=int(input("enter the number"))

    attempt +=1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempt} attempts!")


