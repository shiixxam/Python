# 7.	File Reading Line by Line with 'with': Open a file using the 'with' statement and read its content line by line, printing each line.

with open("B:\python learning\Day9\Reading\shivam.txt", "r") as file:

    for line in file:
        print(line.strip())
        
