class User:

    bank_name = "First National Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, amount, recipient):
        self.make_withdrawl(amount)
        recipient.make_deposit(amount)
        return self

ed = User("Edward Elric", "fullmetalalchemist@amestris.gov")
al = User("Alphonse Elric", "aelric@rockbellautomail.com")
winry = User("Winry Rockbell", "wrockbell@rockbellautomail.com")

ed.make_deposit(250).make_deposit(350).make_deposit(500).make_withdrawl(42).display_user_balance()
winry.make_deposit(1250).make_deposit(2500).make_withdrawl(500).make_withdrawl(367).display_user_balance()
al.make_deposit(250).make_withdrawl(25).make_withdrawl(15).make_withdrawl(100).display_user_balance()
