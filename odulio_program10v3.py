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
        self.label = 0
    def deposit(self, amount):
        amount = 0
        self.label= self.label + amount
    def withdraw(self, amount):
        if self.label > 0:
            amount = 0
            self.label = self.label - amount
   
    def transfer(self, amount, ID):
        if self.label > 0:
            amount = 0
            self.label = self.label






def main():
    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
main()
