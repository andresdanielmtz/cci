from collections import defaultdict

transactions = [
    { "name": "andres", "expense": 100 },
    { "name": "ramon", "expense": 50 },
    { "name": "andres", "expense": 50 },
]

def get_expense(item):
    name, expense = item
    return expense

# K = 1 by default
def calculateTransactions(transactions, k = 1):
    res = defaultdict(int) # str -> int
    TRANSACTION_EXPENSE_LIMIT = 50
    
    for transaction in transactions:
        name = transaction["name"]
        expense = transaction["expense"]
        
        if expense > TRANSACTION_EXPENSE_LIMIT:
            res[name] += expense
    
    # Get K most
    items = list(res.items())
    items.sort(key=get_expense, reverse=True)
    top_k = items[:k]
    
    return top_k

result = calculateTransactions(transactions)
print(result)