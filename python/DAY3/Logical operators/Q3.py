# 3.	Logical NOT: Ask the user if they are a student ( True or False ) and use the not operator to print the opposite (whether they are not a student).



student = input("Are you a student? (True or False): ").lower() == "true"

if not student:
    print("You are a not student.")
else:
    print("You are  a student.")


