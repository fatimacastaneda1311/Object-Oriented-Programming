# Class AgeTooSmallError is raised when the input age is below the allowed threshold (18 years).
class AgeTooSmallError(Exception):
    """Exception raised when the input age is below the allowed threshold"""
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}"
        super().__init__(message)

# Class AgeTooLargeError is raised when the input age is above the allowed threshold (120 years).
class AgeTooLargeError(Exception):
    """Exception raised when the input age is above the allowed threshold"""
    def __init__(self, age, threshold=120):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is above the allowed threshold of {threshold}"
        super().__init__(message)

# Function to check the age against defined thresholds
def check_age(age):
    """Checks if the age meets the valid range requirements"""
    if age < 18:
        raise AgeTooSmallError(age)
    elif age > 120:
        raise AgeTooLargeError(age)
    print("Access granted")

# Example Usage (Try-Except Block)
try:
    # The value "abc" can be replaced with input() or any test value (e.g., 15, 130, or 25)
    user_input = "abc"
    age_value = int(user_input)
    check_age(age_value)
except ValueError as err:
    print(f"ValueError caught: Invalid non-integer input. Details: {err}")
except AgeTooSmallError as err:
    print(f"Custom exception caught: {err}")
except AgeTooLargeError as err:
    print(f"Custom exception caught: {err}")
finally:
    print("Code processing finished!")