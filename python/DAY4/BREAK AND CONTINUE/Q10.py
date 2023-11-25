# 10.	Continue with Even Numbers: Write a program that prints numbers from 1 to 20 but skips odd numbers using the continue statement.


for number in range(1, 21):  
    if number % 2 != 0: 
        continue  
    print(number)
