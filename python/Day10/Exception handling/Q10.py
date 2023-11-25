# 10.	Resource Release with 'finally': Demonstrate the use of the 'finally' block to release resources like file handles or database connect



try:

    with open("B:\python learning\Day10\Exception handling\shibam.txt","w") as file:
        a=file.write("hello,this is a simple message through file handling..........................")

    print(a)
except ValueError:
    print("value error occurred")
finally:
    if "a" in locals:
        file.close()    
