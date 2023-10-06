# 7.	Guess the Word: Implement a word-guessing game where the user has to guess a word. Use a while loop with the break statement to end the game when the word is guessed correctly.




word = "shivam"

while True:
    guess = input("Guess the word: ").lower()  
    
    if guess == word:
        print("Congratulations! You guessed the word correctly.")
        break  
    else:
        print("Incorrect guess. Try again.")
