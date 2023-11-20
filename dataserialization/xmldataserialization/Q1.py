#  <!-- Create an XML document representing a list of books with attributes such as title, author, and genre. Write a Python program that parses this XML document and displays the book titles along with their authors. -->




import xml.etree.ElementTree as ET

tree =ET.parse("B:\\python learning\\dataserialization\\xmldataserialization\\Q1.xml")
root=tree.getroot()


for book in root.findall("book"):
    title=book.find("title").text
    author=book.find("author").text
    genre=book.find("genre").text


    print(f"title:{title}, author: {author}, genre:{genre}")