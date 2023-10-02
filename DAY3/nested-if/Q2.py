# 9.	Ticket Pricing: Create a program that asks the user for their age and whether they have a student ID. Use nested if-else statements to determine the ticket price based on age and student status. Print the ticket price




age = int(input("Enter your age: "))

student_id = input("Do you have a student ID? (yes or no): ").lower()

ticket_price = None

if age < 5:
    ticket_price = 0 
if age >= 5 and age <= 12:
    if student_id == "yes":
        ticket_price = 10  
    else:
        ticket_price = 15  
if age > 12:
    if student_id == "yes":
        ticket_price = 15 
    else:
        ticket_price = 20  

print(f"The ticket price is {ticket_price}")
