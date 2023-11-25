# 1.	Question: What is a class in Python, and why is it used?





class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks!")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  


# In this example, the Dog class defines attributes (name and breed) and methods (bark()). 
# You can create instances of the Dog class (objects) and interact with them using the defined methods and attributes.