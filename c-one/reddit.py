# Find occurrence of a char count between some subrange of a string 

s = "aabbcdasdsa"
l = 6
r = len(s) # the end of the string
letter = "a"

def getCountOccurrencesInSubstring(s, l, r, letter) -> int:
    count = 0
    for i in range(l, r):
        char = s[i]
        if char == letter:
            count += 1
    return count

counter = getCountOccurrencesInSubstring(s, l, r, letter)
print(f"Counter: {counter}")

'''
 Given a data set of transactions and my job was to parse and sort by date of transaction, by company, and best cashback offer 
'''

transactions = [
    {
        "transaction_id": "t1",
        "date": "2026-03-01",
        "company": "Amazon",
        "amount": 120.50,
        "cashback": 0.05  # 5%
    },
    {
        "transaction_id": "t2",
        "date": "2026-03-03",
        "company": "Walmart",
        "amount": 75.00,
        "cashback": 0.02
    },
    {
        "transaction_id": "t3",
        "date": "2026-02-28",
        "company": "Amazon",
        "amount": 200.00,
        "cashback": 0.03
    },
    {
        "transaction_id": "t4",
        "date": "2026-03-02",
        "company": "Target",
        "amount": 60.00,
        "cashback": 0.04
    },
    {
        "transaction_id": "t5",
        "date": "2026-03-01",
        "company": "Walmart",
        "amount": 150.00,
        "cashback": 0.01
    }
]

def parseTransactions(transactions) -> list:
    transactions_sorted_by_date = sorted(transactions, key = lambda elem: elem["date"], reverse=True)
    transactions_sorted_by_company = sorted(transactions, key = lambda elem: elem["company"], reverse=True)
    transactions_sorted_by_cashback = sorted(transactions, key = lambda elem: elem["cashback"], reverse=True)
    
    return [transactions_sorted_by_date[0], transactions_sorted_by_company[0], transactions_sorted_by_cashback[0]]

res = parseTransactions(transactions)
print(res)

