class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Amount {amount} deposited. Current balance is {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Amount {amount} withdrawn. Current balance is {self.balance}"
        else:
            return "Insufficient funds"

    def check_balance(self):
        return f"Current balance is {self.balance}"


if __name__ == "__main__":
    accounts = {}

    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_name = input("Enter account name: ")
            accounts[account_name] = BankAccount()
            print("Account created successfully.")

        elif choice == 2:
            account_name = input("Enter account name: ")
            amount = float(input("Enter amount to deposit: "))
            if account_name in accounts:
                print(accounts[account_name].deposit(amount))
            else:
                print("Account not found.")

        elif choice == 3:
            account_name = input("Enter account name: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_name in accounts:
                print(accounts[account_name].withdraw(amount))
            else:
                print("Account not found.")

        elif choice == 4:
            account_name = input("Enter account name: ")
            if account_name in accounts:
                print(accounts[account_name].check_balance())
            else:
                print("Account not found.")

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")

