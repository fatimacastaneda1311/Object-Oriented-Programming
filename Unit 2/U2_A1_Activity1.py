### Create a class named Car with the following attributes: brand, model, and color.
# Add a method called show_info() that prints the full information of the car.
# Then, create two objects of the Car class with differenct values and call the method to
# display their information.

class Car:
    """A class representing a car with brand, model, and color attributes."""
    def __init__(self, brand, model, color):  # Initialize the instance with brand, model, and color
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):  # Display the full information of the car
        print(f"Car -> Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

# Creating instances of the Car class and displaying their information
car1 = Car("Chevrolet", "Spark", "Green")
car2 = Car("Cadillac", "CTS", "Black")

# Displaying information of the cars
car1.show_info()
car2.show_info()

### POSSIBLE ERRORS:
# 1. Forget "self" in method parameters.
# 2. Fail to initialize the attributes in __init__.