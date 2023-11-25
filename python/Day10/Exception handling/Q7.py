# 7.	Resource Cleanup with 'finally': Open a file for writing and ensure it is properly closed using the 'finally' block.




try:
    with open("shivam.txt","w") as file:
        a=file.write("hello !!!!")
        print(a)
except Exception as e:
    print(f"an error occured{e}")
finally:
    if file is locals():
        file.close()