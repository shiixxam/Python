#  10. Table Formatting: Format data into a table with columns and rows.



data = [("1", "Sakshi"), ("2", "Mansi"), ("3", "Bhavesh")]
print("-" * 30)
print("{:<15} {:<15}".format("ID", "Name"))
for row in data:
    print("{:<15} {:<15}".format(row[0], row[1]))

    