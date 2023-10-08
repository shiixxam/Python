#  6. Date Formatting: Format a date string in a readable format (e.g., "YYYY-MM-DD" to "MM/DD/YYYY").


x = "30-05-2002"
print(x)
y = "{}/{}/{}".format(x[0:2], x[3:5], x[6:10])
print("Formatted date:", y)




