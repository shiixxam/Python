# 9.	Circle Area and Circumference: Request the radius of a circle from the user. Calculate both the area and circumference of the circle using the formulas (Area = π r^2 and Circumference = 2 π * r). Print the results.




radius = float(input("enter the radius of circle :"))

pi_value = 3.14

area= pi_value * radius**2

cirucmference = 2 * pi_value * area

print(f"the area of circle with radius {radius} is  {area}")
print(f"the circumference of the radius {radius} is  {cirucmference}")