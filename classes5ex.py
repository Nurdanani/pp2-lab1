class account:
    def __init__(self , owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.balance=0
        
    def deposit(self,amount ):
        self.balance += amount
        print(f'{amount} deposited, new balance:{self.balance}')
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} withdrawn , new balance: {self.balance}')
        else:
            print(' Withdrawal cannot be processed.')


my_account = account("nnn")
my_account.deposit(100)
my_account.withdraw(200)
