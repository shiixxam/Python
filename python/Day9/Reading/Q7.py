# 7. File Copy: Copy the content of one file to another file. 

# 1) Create one file 
# 2) Add values to new file
# 3) create a new file 
# 4) add values from one file to another


with open("B:\python learning\Day9\Reading\shibam.txt","r") as source_file:
        content=source_file.read()



with open("B:\python learning\Day9\Reading\harsh.txt", "w") as destination_file:
        destination_file.write(content)
        


