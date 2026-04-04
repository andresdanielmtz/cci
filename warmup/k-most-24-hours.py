from collections import defaultdict
from datetime import datetime, date
import time 
import heapq

purchases = [
    {"user_id": "andres", "amount": 120.50, "timestamp": 1775174400},  # Apr 3, 2026 00:00:00
    {"user_id": "sofia",  "amount": 75.00,  "timestamp": 1775178000},  # Apr 3, 2026 01:00:00
    {"user_id": "andres", "amount": 200.00, "timestamp": 1775181600},  # Apr 3, 2026 02:00:00
    {"user_id": "leo",    "amount": 15.75,  "timestamp": 1775203200},  # Apr 3, 2026 08:00:00
    {"user_id": "sofia",  "amount": 300.00, "timestamp": 1775210400},  # Apr 3, 2026 10:00:00
    {"user_id": "maria",  "amount": 500.00, "timestamp": 1775214000},  # Apr 3, 2026 11:00:00
    {"user_id": "andres", "amount": 50.00,  "timestamp": 1775260800},  # Apr 4, 2026 00:00:00
]

# 24 hours into seconds
TIME_LIMIT = 86_400

# Build 

# create a minheap
# only store those which are in todays date 

K = 3 # Get the 3 with the biggest amounts spent.

def getHighestPurchasers(purchases, k):
    transactions = defaultdict(list)
    for purchase in purchases:
        user_id = purchase["user_id"]
        
        # should only store those for today
        timestamp = purchase["timestamp"]
        
        today_timestamp = time.time()
        if today_timestamp - timestamp <= TIME_LIMIT:
            transactions[user_id].append(purchase["amount"])
            
    totals = []
    for user, amounts in transactions.items():
        total_spent = sum(amounts)
        totals.append((user, total_spent))
    
    totals.sort(key = lambda total: total[1], reverse = True)
    print(totals[:k])
getHighestPurchasers(purchases, K)