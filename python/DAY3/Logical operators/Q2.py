# 2.	Discount Eligibility: Create a program that asks the user if they have a membership card ( True or False ) and if the total purchase amount is above $50. Use the or operator to determine if they are eligible for a discount. Print the result.






have_membership = input("do uh have member ship card (True or false ):").lower()
purchase_amt=float(input("enter the total amout of purchase "))

eligible = have_membership or purchase_amt > 50

if eligible:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
