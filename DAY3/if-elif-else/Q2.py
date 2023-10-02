# 7.	Day of the Week: Prompt the user for a number representing a day of the week (1 for Monday, 2 for Tuesday, etc.). Use if-elif-else statements to print the corresponding day's name.








day = int(input("Enter a number (1 for Monday, 2 for Tuesday, etc.): "))

if day == 1:
    print ("Monday")
elif day == 2:
    print ("Tuesday")
elif day == 3:
    print ("Wednesday")
elif day == 4:
    print ("Thursday")
elif day == 5:
    print ("Friday")
elif day == 6:
    print ("Saturday")
elif day == 7:
    print ("Sunday")
else:
    print ("Invalid day number")


print(day)
