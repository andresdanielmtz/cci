from collections import defaultdict, Counter

"Return dictionary with total spent per user"

transactions = [
    ("user1", 100),
    ("user2", 200),
    ("user1", 50),
]

total_spent = defaultdict(int)
for transaction in transactions:
    user = transaction[0]
    user_spent = transaction[1]
    total_spent[user] += user_spent

print(total_spent)

"Given a string s, return the first char that appears only once."

s = "aaaasdddddfff"
s_counter = Counter(s)
print(dict(s_counter))

for char in s:
    if dict(s_counter)[char] == 1:
        print(char)
        break

"Valid Parentheses"

string_parentheses = "{}"
remaining = 0
string_counter = defaultdict(int)
string_dict = {
    "}": "{",
    "]": "[",
    ")": "(",
}

stack = []
opening = ["{", "(", "["]
closing = ["}", ")", "]"]

for char in string_parentheses:
    if char in opening:
        stack.append(char)
    elif char in closing:
        if len(stack) > 0:
            key = string_dict[char]
            top = stack[-1]
            if key == top:
                stack.pop()
            else:
                print("Invalid")
                break
        else: 
            print("Invalid")
            break
    print(stack)
    
'''Log processing 
Given logs
Return the user with the highest total activity'''
logs = [
    "user1 100",
    "user2 200",
    "user1 50"
]

logs_dict = defaultdict(int)
for log in logs:
    user_data = log.split()
    user_name = user_data[0]
    user_spent = user_data[1]
    logs_dict[user_name] += int(user_spent)

print(logs_dict)

''' Sliding window average '''

avg_inp = [1, 2, 3, 4, 5]
k = 3

# o(n^2) because of arr[i:i+k]
def getAverage(arr, k):
    res = []
    window_sum = 0
    for i in range(0, len(arr)):
        window_sum += arr[i] # add current value 
        
        if i >= k - 1: # if its more than the limit, remove the first value you added i - (k - 1) 
            res.append(window_sum / k)
            index = i - (k - 1)
            print(index)
            window_sum -= arr[index]
    return res
res_avg = getAverage(avg_inp, k)
print(res_avg)

