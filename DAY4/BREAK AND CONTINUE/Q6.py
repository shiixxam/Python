# 6.	Skip Divisible Numbers: Write a program that prints numbers from 1 to 50, but skips numbers divisible by 3 using the continue statement.





for i in range (1,51):
    if i %3==0:
        continue
    print(i)
    i-=1