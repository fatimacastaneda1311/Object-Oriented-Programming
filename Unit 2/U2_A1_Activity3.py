### Create a class named BankAccount with the following characteristics:
# - A class attribute named bank = "Central Bank"
# - An instance method named show_balance() that prints the client's balance.
# - A class method named show_bank() that prints the bank's name.
# - A static method named convert currency(value) that receives an amount in dollars and
#   converts it to pesos (use a fixed exchange rate of your choice).

class BankAccount:
    """A class representing a bank account with a balance and bank information."""
    bank = "Central Bank"

    def __init__(self, balance):  # Initialize the instance with a balance
        self.balance = balance

    def show_balance(self):  # Display the client's balance
        print(f"Balance: {self.balance}")

    @classmethod  # Display the bank's name
    def show_bank(cls):
        print(f"Bank name: {cls.bank}")

    @staticmethod  # Convert an amount in dollars to pesos using a fixed exchange rate
    def convert_currency(value):               # Method to convert currency from USD to MXN
        exchange_rate = 18.19                  # Fixed exchange rate for USD to MXN (as of oct 2nd, 2026)
        pesos = value * exchange_rate          # Convert the value in dollars to pesos
        return f"${value} USD = ${pesos} MXN"  # Return the conversion result as a formatted string

# Creating an instance of the BankAccount class and demonstrating its methods
bankAccount1 = BankAccount(1000)  # Displaying the client's balance and bank information
bankAccount1.show_balance()       # Displaying the bank's name using the class method
bankAccount1.show_bank()          # Converting an amount in dollars to pesos using the static method
print(BankAccount.convert_currency(6))

### POSSIBLE ERRORS:
# 1. Use @classmethod instead of @staticmethod.
# 2. Use self within a static method (not allowed).
# 3. Fail to define a fixed exchange rate in convert_currency.