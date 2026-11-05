class TypesOfException:
    """A class designed to encapsulate data structures and methods that intentionally
    trigger and handle Python's most common built-in exceptions."""

    def __init__(self):
        """Initializes the class attributes with a sample list and a sample dictionary
        to facilitate IndexError and KeyError demonstrations later."""
        # A list containing three integer elements (valid indices: 0, 1, 2)
        self.list = [10, 20, 30]
        # A dictionary containing sample user data (valid keys: 'username', 'age')
        self.dict = {"username": "Ana", "age": 25}

    def value_error(self, value):
        """Attempts to convert a non-numeric string into an integer.
        Raises -> ValueError: Raised when a function receives an argument of the right type but an inappropriate value."""
        # Trying to parse a text string into an integer will raise a ValueError
        return int(value)

    def type_error(self, a, b):
        """Attempts to perform an arithmetic addition between incompatible data types (e.g., an integer and a string).
        Raises -> TypeError: Raised when an operation is applied to an object of an inappropriate type."""
        # Adding an integer and a string together is unsupported in Python
        return a + b

    def zero_division_error(self, divisor):
        """Performs a division operation using a divisor of zero.
        Raises -> ZeroDivisionError: Raised when dividing by zero."""
        # Dividing any number by zero is mathematically undefined and triggers this exception
        return 50 / divisor

    def index_error(self, ind_value):
        """Attempts to access a list element using an index outside its valid range.
        Raises -> IndexError: Raised when accessing an invalid index in a list or tuple."""
        # Accessing an index that does not exist in self.list triggers an IndexError
        return self.list[ind_value]

    def key_error(self, key_value):
        """Attempts to look up a key that does not exist inside the dictionary.
        Raises -> KeyError: Raised when accessing a non-existent key in a dictionary."""
        # Searching for a key absent from self.dict triggers a KeyError
        return self.dict[key_value]

# Main Program Execution
if __name__ == "__main__":
    # Instantiate the exception handler demonstration object
    errs = TypesOfException()

    # 1. Demonstration of ValueError
    try:
        # Passing "abc", which cannot be parsed into a base-10 integer
        errs.value_error("abc")
    except ValueError as eg:
        print(f"[CAUGHT] ValueError successfully handled: {eg}")
        print("Explanation: Received a string instead of a valid numeric value\n")

    # 2. Demonstration of TypeError
    try:
        # Trying to add an integer (10) and a string ("text") together
        errs.type_error(10, "text")
    except TypeError as eg:
        print(f"[CAUGHT] TypeError successfully handled: {eg}")
        print("Explanation: Operation applied to objects of inappropriate types\n")

    # 3. Demonstration of ZeroDivisionError
    try:
        # Passing 0 as the divisor parameter
        errs.zero_division_error(0)
    except ZeroDivisionError as eg:
        print(f"[CAUGHT] ZeroDivisionError successfully handled: {eg}")
        print("Explanation: Division denominator cannot be zero\n")

    # 4. Demonstration of IndexError
    try:
        # Requesting index 10, but the list only goes up to index 2
        errs.index_error(10)
    except IndexError as eg:
        print(f"[CAUGHT] IndexError successfully handled: {eg}")
        print("Explanation: Tried to access an invalid index outside list bounds\n")

    # 5. Demonstration of KeyError
    try:
        # Searching for the key 'email' which has not been defined in the dictionary
        errs.key_error("email")
    except KeyError as eg:
        print(f"[CAUGHT] KeyError successfully handled: {eg}")
        print("Explanation: Tried to look up a non-existent key in the dictionary\n")