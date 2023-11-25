# 9.	String Formatting: Format a phone number or date string in a specific way.


x=input("Enter any phone no: ")
if len(x)==10:
    print("{}-{}-{}".format(x[:3], x[3:6],x[6:]))
else:
    print("enter correct number")