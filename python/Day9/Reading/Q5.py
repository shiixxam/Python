# 5. File Line by Line: Read the file line by line and print each line.


with open("B:\python learning\Day9\Reading\shibam.txt", "r") as file:

    for line in file:
        print(line.strip())
        
