# Create a class Accountant with a method generate_report() that prints "Generating financial report."
# Create a class Technician with a method repair_machine() that prints "Repairing machine."
# Create a class Boss that inherits from both classes and test both methods.

class Accountant:
    """Represents an accountant with a method to generate financial reports."""
    @staticmethod  # Indicates that this method does not depend on instance attributes and can be called on the class itself.
    def generate_report():
        print("Generating financial report.")

class Technician:
    """Represents a technician with a method to repair machines."""
    @staticmethod  # Indicates that this method does not depend on instance attributes and can be called on the class itself.
    def repair_machine():
        print("Repairing machine.")

class Boss(Accountant, Technician):  # Inherits from both Accountant and Technician classes.
    """Represents a boss who can both generate reports and repair machines."""
    pass

# Testing the classes and their methods
acc1 = Accountant()  # Create an instance of the Accountant class.
acc1.generate_report()  # Call the generate_report() method, which prints "Generating financial report."

tech1 = Technician()  # Create an instance of the Technician class.
tech1.repair_machine()  # Call the repair_machine() method, which prints "Repairing machine."

boss1 = Boss()  # Create an instance of the Boss class, which inherits from both Accountant and Technician.
boss1.generate_report()  # Call the generate_report() method from the Accountant class, which prints "Generating financial report."
boss1.repair_machine()  # Call the repair_machine() method from the Technician class, which prints "Repairing machine."

### POSSIBLE ERRORS (May occur if the code is modified incorrectly):
# 1. Forget to inherit from both Accountant and Technician classes in the Boss class definition.
# 2. Method conflicts if both base classes define a method with the same name but different implementations.
# 3. Forget to implement a method required by the program logic.