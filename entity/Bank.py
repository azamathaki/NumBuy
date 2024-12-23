
class Bank:
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance

    def withdraw(self, amount):
        self.initial_balance = self.initial_balance - amount

    def deposit(self, amount):
        self.initial_balance += amount

    def get_balance(self):
        return self.initial_balance

