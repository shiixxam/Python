# Given an existing XML file containing information about students (name, age, grade), write a Python script that parses the XML data and identifies students who are above a certain age threshold. Display the names and ages of these students.


import xml.etree.ElementTree as ET

# Parse the XML file
tree =ET.parse("B:\\python learning\\dataserialization\\xmldataserialization\\Q2.xml")
root = tree.getroot()

# Set the age threshold
age_threshold = 18

# Identify students above the age threshold
students_above_threshold = []
for student in root.findall('student'):
    age = int(student.find('age').text)
    if age > age_threshold:
        students_above_threshold.append(student)

# Display the names and ages of the students above the age threshold
for student in students_above_threshold:
    name = student.find('name').text
    age = int(student.find('age').text)
    print(f"{name} - {age}")
