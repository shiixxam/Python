# 2.	Conditional Return: Create a function that returns "Even" if a given number is even and "Odd" if it's odd.



def func (number):
    if number % 2==0:
        return f"{number} is even number"
    else:
        return f"{number} is odd number"
a=int(input("Enter number: "))
b=func(a)
print(b)

