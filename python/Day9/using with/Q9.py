# 9.	File Writing with 'with' (Binary): Write binary data to a file using the 'with' statement.


binary_data = b'\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64'

with open("B:\python learning\Day9\Reading\shivam.txt","wb") as file:

    file.write(binary_data)