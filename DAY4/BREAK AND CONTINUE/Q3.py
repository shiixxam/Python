# 3.	Password Retry: Implement a password validation system using a while loop. Ask the user to enter a password, and if it's incorrect, give them three attempts using a break statement.


password="shivam"
attempt =3

while attempt>0:
    user=input("enter the password")
    if password==user:
        print("password is correct")
        break
    else:
        print("password is not correct")
        attempt-=1
    if attempt==0:
        print("please try again later,Attempts over!")
