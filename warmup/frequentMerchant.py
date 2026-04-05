from collections import defaultdict

transactions = [
    {"user_id": "andres", "merchant_id": "amazon", "timestamp": 1775174400},
    {"user_id": "andres", "merchant_id": "walmart", "timestamp": 1775178000},
    {"user_id": "sofia", "merchant_id": "nike", "timestamp": 1775178000},
    {"user_id": "andres", "merchant_id": "amazon", "timestamp": 1775181600},
    {"user_id": "andres", "merchant_id": "walmart", "timestamp": 1775188800},
    {"user_id": "sofia", "merchant_id": "nike", "timestamp": 1775174400},
    {"user_id": "andres", "merchant_id": "target", "timestamp": 1775185200},
    {"user_id": "sofia", "merchant_id": "adidas", "timestamp": 1775181600},
]


def getMostFrequentMerchantPerUser(transactions):
    merchants = defaultdict(int)
    for transaction in transactions:
        user_id = transaction["user_id"]
        timestamp = transaction["timestamp"]

        merchants[user_id] = max(merchants["timestamp"], timestamp)
    return merchants


getMostFrequentMerchantPerUser(transactions)
