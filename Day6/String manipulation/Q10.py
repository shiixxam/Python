# 10.	Palindrome Checker: Write a program to check if a given string is a palindrome (reads the same forwards and backwards).

a=input("enter the string")

b=a[::-1]

if a==b:
    print("its palindrome")
else:
    print("its not palindrome")