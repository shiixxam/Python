# 5.	Prime Number Checker: Prompt the user to enter a number and use a while loop to determine if it's a prime number. Print the result.





number = int(input("Enter a number: "))

if number < 2:
    is_prime = False
else:
    is_prime = True
    current_divisor = 2  

    while current_divisor <= number // 2:
        if number % current_divisor == 0:
            is_prime = False
            break  
        current_divisor += 1

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")






