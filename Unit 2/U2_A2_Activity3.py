# Create a function calculate_payment(worker) that calls a method payment() of the past object.
# Create several classes (FullTimeEmployee, HourlyEmployee) each with its own payment() method.
# Test the fuction with differents objects and see how the same method produces different results.

def calculate_payment(worker):
    # Assume that the worker object has a payment() method
    return worker.payment()  # Calls the payment() method of the worker object, which can be an instance of FullTimeEmployee or HourlyEmployee.

class FullTimeEmployee:
    """"Represents a full-time employee with an annual salary."""
    def __init__(self, annual_salary):
        self.annual_salary = annual_salary 

    def payment(self):  # Defines the payment method for full-time employees.
        # Monthly payment is calculated by dividing the annual salary by 12.
        return self.annual_salary / 12 

class HourlyEmployee:
    """Represents an hourly employee with hours worked and hourly rate."""
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def payment(self):  # Defines the payment method for hourly employees.
        return self.hours * self.rate

# Testing the function with the two classes
worker1 = FullTimeEmployee(60000)  # Represents a full-time employee with an annual salary of $60,000. (Can be modified)
worker2 = HourlyEmployee(120, 50)  # Represents an hourly employee who worked 120 hours at a rate of $50 per hour. (Can be modified)

# Testing the calculate_payment function with different worker objects
print(calculate_payment(worker1))  # Prints the monthly payment for the full-time employee
print(calculate_payment(worker2))  # Prints the total payment for the hourly employee

### POSSIBLE ERRORS (May occur if the code is modified incorrectly):
# 1. Forget to define the payment() method in either FullTimeEmployee or HourlyEmployee classes, leading to AttributeError.
# 2. Use the wrong method name when calling the payment() method.
# 3. Forget to pass the correct parameters when creating instances of FullTimeEmployee or HourlyEmployee classes.