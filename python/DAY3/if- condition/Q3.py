# 3.	Vowel Checker: Prompt the user to enter a letter. Use an if statement to determine if it's a vowel (a, e, i, o, u) or a consonant. Print the result.

letter = input("Enter a letter: ")

letter = letter.lower()

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(f"{letter} is a vowel.")
else:                                        #This is If conditional question bt i used if-else for  better understanding .
    print(f"{letter} is a consonant.")



    
