from collections import defaultdict

dic = {"irv": 4127}

print(dic["irv"])
print(dic.get("irv"))
print(dic.get("uhh"))

groups = defaultdict()
groups["fruits"] = ":D"
groups["oranges"] = [1,2,3]

print(dict(groups))

words = ["apple", "ant", "banana", "bat", "carrot", "cat"]
grouped_words = defaultdict(list)
grouped_count = defaultdict(int)
for word in words:
    first_letter = word[0]
    grouped_words[first_letter].append(word)
    grouped_count[first_letter] += 1 # by default it is 0
print(dict(grouped_words))
print(dict(grouped_count))

