class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = pin

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
        else:
            print("Amount must be positive")

    def verify_pin(self, pin):
        return self.__pin == pin

def register():
    username = input("Enter your username: ")
    account_number = input("Enter your account number (10 digits): ")
    while len(account_number) != 10 or not account_number.isdigit():
        print("Account number must be 10 digits.")
        account_number = input("Enter your account number (10 digits): ")
    pin = input("Enter your PIN: ")
    return BankAccount(username, 0, pin)

def login(accounts):
    username = input("Enter your username: ")
    pin = input("Enter your PIN: ")
    for account in accounts:
        if account.account_holder == username and account.verify_pin(pin):
            return account
    print("Invalid username or PIN.")
    return None

def bank_menu(account):
    while True:
        print("\nBank Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Current Balance:", account.get_balance())
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account.set_balance(account.get_balance() + amount)
            print("Deposit successful. Updated Balance:", account.get_balance())
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= account.get_balance():
                account.set_balance(account.get_balance() - amount)
                print("Withdrawal successful. Updated Balance:", account.get_balance())
            else:
                print("Insufficient balance.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Create an instance of BankAccount
accounts = []
accounts.append(register())

# Login and access bank menu
account = login(accounts)
if account:
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            accounts.append(register())
        elif choice == '2':
            account = login(accounts)
            if account:
                bank_menu(account)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
account = BankAccount("John Doe", 1000, 1234)

# Accessing the public attribute
print("Account Holder:", account.account_holder)

# Trying to access the protected and private attributes
print("Balance (protected):", account._balance)
try:
    print("PIN (private):", account.__pin)
except AttributeError as e:
    print(e)

# Using the getter and setter methods
print("Current Balance:", account.get_balance())
account.set_balance(1500)
print("Updated Balance:", account.get_balance())

# Verifying the PIN
print("PIN Verification (correct):", account.verify_pin(1234))
print("PIN Verification (incorrect):", account.verify_pin(4321))