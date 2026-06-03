class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance!")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Create Account
account = BankAccount()

# Menu
while True:
    print("\n===== BANK ACCOUNT MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display_balance()

    elif choice == 4:
        print("Thank you for using the Bank Account System!")
        break

    else:
        print("Invalid Choice!")