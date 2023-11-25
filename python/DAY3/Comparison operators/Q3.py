# 3.	Greater Than or Less Than: Ask the user for their age and compare it to 18 using the greater than (>) and less than (<) operators. Print whether they are older or younger than 18.

age = int(input("Enter your age: "))

if age > 18:
    print("You are older than 18.")
elif age < 18:
    print("You are younger than 18.")
else:
    print("You are exactly 18 years old.")
