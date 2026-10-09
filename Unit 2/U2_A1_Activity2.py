### Create a class name Person with a constructor that receives the parameters name, age,
# and city.
# Add a method called greet() that displays a message such as:
# "Hi, my name is Ana, I am 25 years old, and I live in Mexico."
# Create three objects of the Person class and make each one call the greet() method.

class Person:
    """A class representing a person with name, age, and city attributes."""
    def __init__(self, name, age, city):  # Initialize the instance with name, age, and city
        self.name = name
        self.age = age
        self.city = city

    def greet(self):  # Display a greeting message with the person's information
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.")

# Creating instances of the Person class and greeting them
person1 = Person("Fátima", 18, "Tepic")
person2 = Person("Alexa", 21, "Juarez")
person3 = Person("Arturo", 22, "Tepic")

# Calling the greet method for each person
person1.greet()
person2.greet()
person3.greet()

### POSSIBLE ERRORS:
# 1. Fail to use f-string correctly to interpolate variables.
# 2. Pass of less parameters than the constructor expects.