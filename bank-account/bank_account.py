from threading import Lock
LOCK = Lock()


class BankAccount(object):
    def __init__(self):
        self.is_opened: bool = False

        self.balance: float = 0

    def get_balance(self):
        if not self.is_opened: raise ValueError('Cannot check balance of a closed account7410')
        return self.balance

    def open(self):
        if self.is_opened: raise ValueError('Account is already opened')
        self.is_opened = True
        self.balance = 0

    def deposit(self, amount):
        if not self.is_opened: raise ValueError('User tried to deposit into a closed account')
        if amount <= 0: raise ValueError("User tried to deposit non-positive money")
        with LOCK: self.balance += amount

    def withdraw(self, amount):
        if not self.is_opened: raise ValueError('User tried to withdraw into a closed account')
        if amount <= 0: raise ValueError("User tried to withdraw non-positive money")
        if amount > self.balance: raise ValueError('User tried to withdraw more money than in the account')
        with LOCK: self.balance -= amount

    def close(self):
        if not self.is_opened: raise ValueError('Account is already closed')
        self.is_opened = False
        self.balance = 0
