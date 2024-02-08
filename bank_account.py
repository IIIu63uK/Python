class bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, amount, account):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            account.balance += amount
            return self.balance
        
bank_account_1 = bank_account('John', 1000)
bank_account_2 = bank_account('Jane', 500)
print(bank_account_1.deposit(500))
print(bank_account_1.withdraw(200))
print(bank_account_1.get_balance())
print(bank_account_1.transfer(200, bank_account_2))