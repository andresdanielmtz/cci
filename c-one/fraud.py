from collections import defaultdict

transactions = [
    {"user": "andres", "timestamp": 2},
    {"user": "andres", "timestamp": 20},
    {"user": "andres", "timestamp": 61},
    {"user": "ramon", "timestamp": 10},
]

# List users that traspass 3 transactions in 60 seconds 

TIME_LIMIT_TRANSACTIONS = 60

def detectFrauds(transactions, k = 3):
    directory = defaultdict(list)
    possible_frauds = []
    
    for transaction in transactions:
        name = transaction["user"]
        timestamp = transaction["timestamp"]
        directory[name].append(timestamp)
        
    print(directory)
    # Sliding window of size k

    # for each list of transactions per user, check the list 
    for name, trans in directory.items():
        trans.sort() # sort in place 

        if len(trans) >= k:
            window_transaction = []
            for i in range(0, len(trans)):
                individual_transaction = trans[i]
                window_transaction.append(individual_transaction)
                
                if i >= k - 1:
                    print(window_transaction)
                    first_transaction = window_transaction[0]
                    last_transaction = window_transaction[-1]
                    
                    
                    if last_transaction - first_transaction < TIME_LIMIT_TRANSACTIONS:
                        possible_frauds.append(name)
                    window_transaction.pop(0)
    print(possible_frauds)

detectFrauds(transactions)