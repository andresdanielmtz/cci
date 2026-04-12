import uuid
from enum import Enum
from datetime import datetime

class TransactionType(Enum):
    TRANSFERENCE = 1


INVALID_OPERATION_MSG = "Invalid operation."
INVALID_OPERATION_SAME_ACCOUNT_TRANSFER = "Invalid operation. The Sender and Receivers' IDs are the same."


class Transaction:
    def __init__(self, type_, amount, target_account_id):
        self.type = type_
        self.amount = amount
        self.timestamp = datetime.now()
        self.target_account_id = target_account_id
    def __str__(self):
        return f"( {self.type}, {self.amount}, {self.timestamp}, {self.target_account_id} )"
    def __repr__(self):
        return self.__str__()
class Account:
    def __init__(self, name: str, account_id: str):
        self.account_id = account_id
        self.name = name
        self._balance = 0
        self._transaction_history = []

    def deposit(self, amount: float):
        if amount < 0:
            raise Exception(INVALID_OPERATION_MSG)
        self._balance += amount

    def add_transaction(self, type_, amount, target_account_id):
        transaction = Transaction(type_, amount, target_account_id)
        self._transaction_history.append(transaction)

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise Exception("It is not possible to withdraw the amount you've requested. Please try with a different amount.")
        if amount < 0:
            raise Exception(INVALID_OPERATION_MSG)
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def get_transactions(self, orderedByDate = True):
        if (orderedByDate):
            return sorted(self._transaction_history, key = lambda transaction: transaction.timestamp)
        return self._transaction_history


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name: str) -> str:
        acc_id = str(uuid.uuid4())
        new_account = Account(name, acc_id)
        self.accounts[acc_id] = new_account
        return acc_id

    def get_account(self, account_id: str) -> Account:
        if account_id not in self.accounts:
            raise Exception("Account not found")
        return self.accounts[account_id]

    def transfer(self, from_id: str, to_id: str, amount: float):
        if amount < 0:
            raise Exception(INVALID_OPERATION_MSG)
        if from_id == to_id:
            raise Exception(INVALID_OPERATION_SAME_ACCOUNT_TRANSFER)

        from_acc = self.get_account(from_id)
        to_acc = self.get_account(to_id)

        if not from_acc or not to_acc:
            raise Exception("One of the accounts couldn't be found. Please try again later.")

        from_acc.withdraw(amount)
        to_acc.deposit(amount)

        from_acc.add_transaction(
            TransactionType.TRANSFERENCE,
            amount,
            to_id
        )

        to_acc.add_transaction(
            TransactionType.TRANSFERENCE,
            amount,
            to_id
        )


# Usage example
banamex = Bank()
andres_id = banamex.create_account("Andres")
sofia_id = banamex.create_account("Sofia")

andres_acc = banamex.get_account(andres_id)
sofia_acc = banamex.get_account(sofia_id)

if andres_acc and sofia_acc:
    andres_acc.deposit(100)
    print(andres_acc.get_balance())

    banamex.transfer(andres_id, sofia_id, 50)

    print(andres_acc.get_balance())  # should be 50
    print(sofia_acc.get_balance())   # should be 50
sofiaTransactions = sofia_acc.get_transactions(True)
print([transaction for transaction in sofiaTransactions])