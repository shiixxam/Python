# 3.	Multiplication Challenge: Ask the user to enter a number and then print the multiplication table for that number from 1 to 10.




user_num = int(input("enter a number:"))

for i in range (1,11):
    result=user_num*i
    print(user_num,"x",i,"=",result)
