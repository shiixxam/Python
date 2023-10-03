# 3.	Multiplication Table: Generate and print the multiplication table for a number entered by the user using a for loop.



user=int(input("enter the number of which table uh want "))

for i in range(1,11):
    result=user * i
    # print(result)

    print(f"{user} x {i}={result}")