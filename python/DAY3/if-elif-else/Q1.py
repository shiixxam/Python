# 6.	Grading System: Ask the user for their test score. Use if-elif-else statements to assign a letter grade (A, B, C, D, or F) based on score ranges. Print the letter grade.



marks =int(input("enter your marks"))

if marks >=80:
    print("YOU GOT GRADE A")
elif marks >=70:
    print("YOU GOT GRADE B")
elif marks >=50:
    print("YOU GOT GRADE C")
elif marks >=40:
    print("YOU GOT GRADE D")
elif marks >=35:
    print("YOU GOT GRADE E")
else:
    print("u r fail")

