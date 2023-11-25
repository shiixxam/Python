# 9.	Infinite Loop with Break: Create an infinite loop that keeps asking the user to enter a number. Use the break statement to exit the loop when the user enters a specific value (e.g., 0).



while True:
    number = int(input("Enter a number (enter 0 to exit): "))
    
    if number == 0:
        print("Exiting the loop.")
        break
