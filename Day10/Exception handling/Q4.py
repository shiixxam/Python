# 4.	Multiple Exceptions: Write a program that attempts to open a file, perform a division, and access a list element. Handle the relevant exceptions using multiple except blocks.

try:
    file=open("shivam.txt","r")
    result=10/0

    my_list = [1, 2, 3]
    element = my_list[5]

except FileNotFoundError:
    print("File not found. Handle the file not found exception.")
except ZeroDivisionError:
    print("Division by zero is not allowed. Handle the division by zero exception.")
except IndexError:
    print("Index out of range. Handle the index error.")
except Exception as e:
    print(f"An error occurred: {e}")







