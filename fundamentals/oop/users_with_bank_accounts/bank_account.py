class BankAccount:
    # class atrribute
    all_accounts = []

    # don't forget to add some default values for these parameters!
    # Default int_rate: 3, default balance: 0
    
    def __init__(self, int_rate = 0.3, balance = 0):
        # your code here! (remember, instance attributes go here)
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon

    @classmethod
    def retrieve_accounts(cls):
        for account in cls.all_accounts:
            print(f"Interest Rate: {100 * account.int_rate}%, Balance: ${account.balance}")

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")

        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        
        return self