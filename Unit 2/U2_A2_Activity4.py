# Create a class Engine with a method start() that prints "Engine started."
# Create a class Car that has an attribute engine (type Engine) 
# and a method start_car() that calls engine.start().

class Engine:
    """Represents a car engine with a method to start it."""
    def start(self):  # Defines the start method for the Engine class.
        print("Engine started")  # Prints "Engine started" when the start() method is called.

class Car:
    """Represents a car that has an engine and can start it."""
    engine = Engine()  # Composition: Car has an Engine object as an attribute.
    def start_car(self):  # Defines the start_car method for the Car class, which starts the engine.
        # Delegating the start operation to the Engine class.
        self.engine.start()  # Calls the start() method of the Engine class to start the engine when start_car() is called.

# Testing the classes and their methods
car1 = Car()  # Create an instance of the Car class.
car1.start_car()  # Call the start_car() method, which in turn calls the start() method of the Engine class.

### POSSIBLE ERRORS (May occur if the code is modified incorrectly):
# 1. Passing None as the engine → AttributeError when calling self.engine.start(); validate in __init__ or raise ValueError.
# 2. Confusing inheritance with composition: if the vehicle has an engine, use composition; if it is an engine (rare), use inheritance.
# 3. Forgetting to call the start() method of the Engine class in the start_car() method of the Car class, leading to no output when starting the car.