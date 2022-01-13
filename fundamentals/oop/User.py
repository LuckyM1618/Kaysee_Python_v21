class User:

    bank_name = "First National Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, amount, recipient):
        self.make_withdrawl(amount)
        recipient.make_deposit(amount)

ed = User("Edward Elric", "fullmetalalchemist@amestris.gov")
al = User("Alphonse Elric", "aelric@rockbellautomail.com")

ed.display_user_balance()
al.display_user_balance()

ed.make_deposit(1618)
ed.display_user_balance()

ed.make_withdrawl(618)
ed.display_user_balance()

ed.transfer_money(250, al)
ed.display_user_balance()
al.display_user_balance()
