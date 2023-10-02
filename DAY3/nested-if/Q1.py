# 8.	Triangle Type: Request the lengths of three sides of a triangle from the user. Use nested if-else statements to determine if it's equilateral (all sides equal), isosceles (two sides equal), or scalene (all sides different). Print the result.






side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 == side2 and side2 == side3:
    print( "triangle is equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("triangle is isosceles") 
else:
    print( "triangle is scalene")


