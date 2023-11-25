# 5.	Type Conversion (int to str): Take an integer input from the user and convert it into a string. Then, print the string.


#1

user_input = int(input("Enter an integer: "))


user_input_str = str(user_input)


print("The integer as a string:", user_input_str)
print(type(user_input_str))


#2




a=int(input("enter the number:"))           #ek variable lo jisme user se number input lo
b=str(a)                                    #ek variable lo jo user input ko string mai covert karde
print(b)                                    #print the string
print(type(b))                              #use type method jise uska type pata chalega vo string float ya integer hai.  


#USING TRY EXCEPT 
#3

a=int(input("enter the number:")) 
try:
    b=str(a)
    print(b)
    print(type(b))
except ValueError:
    print("enter theb valid integer.")



