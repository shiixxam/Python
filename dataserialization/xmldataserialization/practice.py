import xml.etree.ElementTree as ET

tree =ET.parse("B:\\python learning\\dataserialization\\xmldataserialization\\practice.xml")
root = tree.getroot()


for person in root.findall("person"):
    name =person.find("name").text
    age=int(person.find("age").text)
    city=person.find("city").text



    print(f"name: {name}, age: {age}, city: {city}")