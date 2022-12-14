"""
Programming Fundamentals
Program 10 - BankAccount class, model solution

Rocko Graziano, UMA
"""

class BankAccount():
    def __init__(self, label):
        self._label = label
        self._balance = 0

    def deposit(self, amount):
        if amount <0:
            print("${:0.2f} Illegal Deposit amount".format(amount))
        else:
            print(f'Depositing ${amount} to {self}')
            self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            print(f"Withdrawl of ${amount:0.2f} Exceeds Balance of ${self._balance:0.2f}")
            return 0
        else:
            print(f'Withdrawing ${amount} from {self}')
            self._balance -= amount
            return amount

    def balance(self):
        return self._balance

    def transfer(self, amount, ID):
        print(f'Transfering ${amount} from {self} to {ID}')
        self.withdraw(amount)
        ID.deposit(amount)

    def __str__(self):
        return self._label

