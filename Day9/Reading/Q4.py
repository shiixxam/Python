# 4. File Line Count: Determine and print the number of lines in the file.


with open("B:\python learning\Day9\Reading\shibam.txt", "r") as file:
    count=0

    for line in file:
        count+=1
print(count)




#wnt to check the length of it then uh will go with len() function



with open("B:\python learning\Day9\Reading\shibam.txt", "r") as file:
    lines=file.read()

line_count=len(lines)

print(line_count)