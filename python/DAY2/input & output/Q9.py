# 9.	Countdown Timer: Request a number from the user and use a loop to count down from that number to 1, printing each number.


user_num=int(input("enter the number :"))

if user_num <=0:
    print("enter a positive number:")
else:
    while user_num >=1:
        print(user_num)
        user_num -=1


