# 2.	Skip Odd Numbers: Write a program that prints all even numbers from 1 to 20, skipping odd numbers using the continue statement.


for number in range(1, 21):
    if number % 2 != 0:
        continue 

    print(number)
