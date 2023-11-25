# 3.	Factor Finder: Take a number from the user and use a while loop to find and print all its factors.



number=int(input("enter the number : "))

factor=1


print(f"Factors of {number}:")
while factor <= number:
    if number % factor == 0:
        print(factor)
    factor += 1


