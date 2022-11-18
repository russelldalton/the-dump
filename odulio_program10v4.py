import time
"""
program: odulio_program10.py
name: Jobe Odulio
description:bank account
date:
notes:
"""
#bank account class
class BankAccount:
    def __init__(self, label):
        self.label = label
        self.amount = 0
    def deposit(self, amount):
        self.amount += amount
        self.label= self.label + amount
    def withdraw(self, amount):
        if self.label > 0:
            self.amount = amount
            self.label = self.label - amount
   
    def transfer(self, amount, ID):
        if self.label > 0:
            self.amount = amount
            self.label += self.amount
            ID.amount -= self.label






def main():
    n = 500
    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
main()
