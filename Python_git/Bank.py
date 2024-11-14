accountlist = []

class Account:
    def __init__(self, account_holder, account_number, account_bal):
        self.account_holder = account_holder
        self.account_number = int(account_number)
        self.account_bal = float(account_bal)
        self.transactions = []
        self.transactions.append(('Initial Balance', account_bal))

    def deposit(self, amount):
        if amount > 0:
            self.account_bal += amount
            self.transactions.append(('Deposit', amount, self.account_bal))
            print(f"${amount} deposited. New balance is: ${self.account_bal}")
        else:
            print("Please provide a valid amount")

    def withdraw(self, amount):
        if amount > self.account_bal:
            print("Insufficient funds")
        else:
            self.account_bal -= amount
            self.transactions.append(('Withdrawal', amount, self.account_bal))
            print(f"${amount} withdrawn. New balance is: ${self.account_bal}")

    @classmethod
    def create_account(cls):
        account_holder = input("Enter account holder name: ")
        account_number = input("Enter account number: ")
        account_bal = input("Enter account balance: ")
        new_account = Account(account_holder, account_number, account_bal)
        accountlist.append(new_account)
        print("Account created successfully")

    def check_balance(self):
        print(f"The current balance is: ${self.account_bal}")
        return self.account_bal

    def account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.account_bal}")
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

def display_all_accounts():
    if accountlist:
        print(f"\nTotal Accounts: {len(accountlist)}")
        for account in accountlist:
            print(f"Account Holder: {account.account_holder}, Account Number: {account.account_number}, Balance: ${account.account_bal}")
    else:
        print("\nNo accounts available.")

def find_account(account_number):
    for account in accountlist:
        if account.account_number == account_number:
            return account

def login():
    acc_number = int(input("Enter account number to log in: "))
    account = find_account(acc_number)
    if account:
        print(f"Login successful! Welcome, {account.account_holder}.\n")
        return account
    else:
        print("Account not found.")

def menu():
    while True:
        print("=====  Menu =====\n")
        print("1. Create account")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Account.create_account()
            display_all_accounts()
        elif choice == 2:
            account = login()
            if account:
                while True:
                    print("\n===== Account Menu =====")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Account Information")
                    print("5. Log Out")

                    acc_choice = int(input("Enter your choice: "))

                    if acc_choice == 1:
                        amount = float(input("Enter amount: "))
                        account.deposit(amount)
                    elif acc_choice == 2:
                        amount = float(input("Enter amount: "))
                        account.withdraw(amount)
                    elif acc_choice == 3:
                        account.check_balance()
                    elif acc_choice == 4:
                        account.account_info()
                    elif acc_choice == 5:
                        print("Logging out...\n")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == 3:
            print("Exiting the bank system.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
