# # 5.	String Repeater: Request a string and a number from the user. Then, print the string repeated that number of times.


a = input("Enter a string: ")
b = int(input("Enter a number: "))


if b < 1:
    print("Number should be greater than or equal to 1.")
else:
    repeated= (a + ' s') * b   #give  space btwn '' - ' ' so the output will be not seperated.
    print(repeated)



