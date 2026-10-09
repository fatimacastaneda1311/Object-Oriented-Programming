# Create a class Employee withb attributes name and salary, 
# and a method show_info() that prints the name and salary.
# Then create a class Manager that inherits from Employee and adds an attribute department.
# Override show_info() to also display the department.

class Employee:
    """Represents an employee with a name and salary."""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    """Represents a manager, who is an employee with a department."""
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

# Create instances of Employee and Manager classes
employee1 = Employee("Arturo", 100)
manager1 = Manager("Javier", 250, "Accounting")

# Call the show_info() method for both instances
employee1.show_info()
manager1.show_info()

### POSSIBLE ERRORS (May occur if the code is modified incorrectly):
# 1. Forget to call the super().__init__() method in the Manager class constructor.
# 2. Forget to call the super().show_info() method in the Manager class show_info() method.
# 3. Printing the salary (float) without using f-strings (e.g., {self.salary:.2f}).