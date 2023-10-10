# 3. File Appending: Append additional text to the file without overwriting the existing content. 


with open ("B:\python learning\Day9\Reading\shibam.txt","a") as file:
    file.write(" this is a new line added through append method.")

with open ("B:\python learning\Day9\Reading\shibam.txt","r") as file:
    content_updated=file.read()
print(content_updated)


