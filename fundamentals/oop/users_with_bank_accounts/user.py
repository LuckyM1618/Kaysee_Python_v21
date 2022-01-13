from bank_account import BankAccount

class User:

    # ***note: throughout the class "account_num" is taken in as the parameter, but then subtracted from to get what would be the account_index, which doesn't explicitly exist. I chose this for theoretical end-user intuitiveness; accounts are 0-indexed in the list, but no one would have an Account 0 

    bank_name = "First National Dojo"

    def __init__(self, name, email_address, num_accounts = 1):
        self.name = name
        self.email = email_address
        self.accounts = []
        for i in range(num_accounts):
            self.accounts.append(BankAccount(int_rate = 0.02, balance = 0))

    def make_deposit(self, account_num = 1, amount = 0):
        self.accounts[account_num - 1].deposit(amount)

        return self

    def make_withdrawl(self, account_num = 1, amount = 0):
        self.accounts[account_num - 1].withdraw(amount)

        return self

    def display_user_balances(self):
        print(f"User: {self.name}")

        print("Accounts:")
        for i in range(len(self.accounts)):
            print(f"Account {i + 1} Balance: ${self.accounts[i].balance}")

        return self

    def transfer_money(self, account_num = 1, amount = 0, recipient = None, rec_account_num = 1):
        self.make_withdrawl(account_num, amount)
        recipient.make_deposit(rec_account_num, amount)

        return self

    # test function
    def display_accounts(self):
        for i in range(len(self.accounts)):
            print(f"Balance: {100 * self.accounts[i].int_rate}, Balance: ${self.accounts[i].balance}")

# ed = User("Edward Elric", "fullmetalalchemist@amestris.gov")
# al = User("Alphonse Elric", "aelric@rockbellautomail.com")
# winry = User("Winry Rockbell", "wrockbell@rockbellautomail.com")

# ed.make_deposit(250).make_deposit(350).make_deposit(500).make_withdrawl(42).display_user_balance()
# winry.make_deposit(1250).make_deposit(2500).make_withdrawl(500).make_withdrawl(367).display_user_balance()
# al.make_deposit(250).make_withdrawl(25).make_withdrawl(15).make_withdrawl(100).display_user_balance()

ed = User("Edward Elric", "fullmetalalchemist@amestris.gov", 3)
al = User("Alphonse Elric", "aelric@rockbellautomail.com", 1)

ed.make_deposit(1,500).display_user_balances()
ed.make_withdrawl(1,250).display_user_balances()

al.make_deposit(amount=200).display_user_balances()

ed.transfer_money(1,200,al,1).display_user_balances()
al.display_user_balances()
