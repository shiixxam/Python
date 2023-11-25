# 1.	Age and Height Check: Write a program that asks the user for their age and height (in centimeters). Use the and operator to check if they are both older than 18 and taller than 160 cm. Print whether they meet both conditions.



age=int(input("enter our age"))
height=float(input("enter your height in centimeters"))

if age >=18 and height >= 160:
    print("u r meet with our requiremnet")
else:
    print("sry u r not 18 and your height is not capable for requirment")

