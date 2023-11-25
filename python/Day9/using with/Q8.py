# 8.	File Copy with 'with': Use the 'with' statement to copy the content of one file to another file.


with open("B:\python learning\Day9\Reading\shivam.txt","r") as source_file:
        content=source_file.read()



with open("B:\python learning\Day9\Reading\harsh.txt", "w") as destination_file:
        destination_file.write(content)
        

