# 10. File Handling Errors: Handle exceptions that may occur when working with files (e.g., file not found). 



try:
    with open("B:\python learning\Day9\Reading\shiva.txt","r") as source_file:
        content=source_file.read()

except FileNotFoundError as e:
    print(f"An error occurred:{e}")
else:
    print(f"File read successfully")

