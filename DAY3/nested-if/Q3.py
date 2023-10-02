# 10.	Character Classifier: Ask the user to input a character (letter, digit, or special character). Use nested if-else statements to classify it as a letter, digit, or special character. Print the classification.


user=input("enter a character")


classification = None

if user.isalpha():
    classification = "letter"
else:
    if "0" <= user <= "9":
        classification = "digit"
    else:
        classification = "special character"

print(f"The character '{user}' is classified as a {classification}.")
