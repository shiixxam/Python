    # 6.	Number Reversal: Take a number from the user and use a while loop to reverse its digits and print the reversed number.





# var = int(input("Enter any number: "))
# reversed_num = 0
# while var != 0:
#     digit = var % 10
#     reversed_num = reversed_num * 10 + digit
#     var //= 10
# print("Reversed Number: " ,reversed_num)




num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print("The reversed number is:", reversed_num)
