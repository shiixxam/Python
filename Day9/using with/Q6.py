# 6.	Exception Handling with 'with': Use the 'with' statement to handle exceptions that may occur when performing an operation.



try:
    with open("B:\python learning\Day9\Reading\shiva.txt","r") as source_file:
        content=source_file.read()

except Exception as e:
    print(f"An error occurred:{e}")
else:
    print(f"File read successfully")

    