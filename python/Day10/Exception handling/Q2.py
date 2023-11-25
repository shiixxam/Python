# 2.	File Reading Error Handling: Open a non-existent file for reading and handle the file not found exception using try-except.




try:
    file="shivam.txt"
    with open(file,"r")as file:
        content = file.read()
        print(content)
except FileNotFoundError:
        print(f"the file {file} was not found")
except Exception as e :
     print(f"an error occurred:{str(e)}")





