import random

'''
 Design a simple bank account class with deposit, transfer, and withdraw functionality using object-oriented programming. Interviewer was more interested in how I talked through my solution, and how I took care of edge cases - even though interviewer did not want me to implement functionality to take care of the edge cases.
'''


class BankAccount:
    def __init__(self):
        self.id = random.randint(0, 100) # todo: update this
        self.amount = 0
    
    def deposit(self, amountToDeposit):
        self.amount += amountToDeposit

    def getAmount(self):
        return self.amount
    
    def withdraw(self, amountToWithdraw):
        if self.amount - amountToWithdraw < 0:
            print("It is not possible")
        else:
            self.amount -= amountToWithdraw
            
    def transfer(self, recipientAccount: "BankAccount", amount: float):
        recipientAccount.deposit(amount)
        self.amount -= amount

acc = BankAccount()

acc2 = BankAccount()
acc.deposit(100)
acc.transfer(acc2, 50)
amountAfterTransfer = acc.getAmount()
acc2AfterTransfer = acc2.getAmount()
print(amountAfterTransfer)
print(acc2AfterTransfer)