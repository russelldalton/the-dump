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
        
    def withdraw(self, amount):
        
        self.amount -= amount

    def getBalance(self):
        return self.amount
            
   
    def transfer(self, amount, ID):
        
        self.amount = amount
        self.label += self.amount
        ID.amount -= self.label
    def __str__(self):
        return self.label






def main():
    n = float(500)
    m = float(100)
    o = float(600)
    p = float(100)
    
    checking = BankAccount('checking')
    saving= BankAccount('saving')
    checking.deposit(n)
    print('deposited',n, 'into checking, current balance is ', checking.getBalance()) 
    saving.deposit(m)
    print('deposited', m, 'into saving, current balance is ', saving.getBalance())
    checking.withdraw(o)
    print('withdrew' , o, 'from checking, current balance is', checking.getBalance())
    saving.withdraw(p)
    print('withdrew' , p , 'from savings, current balance is', saving.getBalance())
    

    


    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
if __name__=='__main__':
    main()
