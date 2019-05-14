class BankAccount:

    interest_rate = 0.01
    accounts = []

    def __init__(self, balance=0.00):
        self.balance = balance

    def deposit(self, number):
        self.balance += number
        return self.balance

    def withdraw(self, number):
        self.balance -= number
        return self.balance

    @classmethod
    def create(cls, number=0.0):
        my_account = BankAccount(number)
        cls.accounts.append(my_account)
        return my_account

    @classmethod
    def total_funds(cls):
        sum_of_balances = 0
        for account in cls.accounts:
           sum_of_balances += account.balance
        return sum_of_balances



    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate
    

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0
