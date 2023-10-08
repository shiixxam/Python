# 4.	Sum of Digits: Calculate and print the sum of the digits of a number entered by the user using a while loop.




number = int(input("enter the number :"))
x=0

while (number>0):
    sum=number%10
    x=x+sum
    number=number//10
print(x)
