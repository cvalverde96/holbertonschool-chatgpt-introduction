class Checkbook:
    """
    A class to represent a checkbook with basic deposit, withdrawal, and balance functionalities.
    """

    def __init__(self):
        """
        Initialize the Checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount to the checkbook balance.

        Parameters:
        amount (float): The amount of money to deposit. Must be a positive number.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook balance if sufficient funds are available.

        Parameters:
        amount (float): The amount of money to withdraw. Must be a positive number.

        If the withdrawal amount exceeds the current balance, an error message will be displayed.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function that provides an interface for the user to interact with the Checkbook.
    The user can perform the following actions: deposit, withdraw, check balance, or exit.

    The program continues running until the user selects 'exit'. It handles invalid inputs 
    and ensures proper error handling for non-numeric inputs and negative values.
    """
    cb = Checkbook()
    while True:
        # Prompt the user to enter an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        # Exit the program
        if action.lower() == 'exit':
            break

        # Handle deposit action
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Deposit amount must be positive. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Handle withdrawal action
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Withdrawal amount must be positive. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Handle balance check action
        elif action.lower() == 'balance':
            cb.get_balance()

        # Handle invalid commands
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

