from collections import defaultdict

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

# count frequencies

common_dict = {}
for fruit in fruits: 
    if common_dict.get(fruit) is None:
        common_dict[fruit] = 1
    else:
        common_dict[fruit] += 1
print(common_dict)

def_dict = defaultdict(int)
for fruit in fruits:
    def_dict[fruit] += 1
print(dict(def_dict))

# first non-repeating character 

s = "aabbcddeff"
non_repeating_char_dict = defaultdict(int)

# get a counter of all characters 

# time: o(n)
# space: o(n) (stores all characters within a list + a counter for each char)
for char in s: 
    non_repeating_char_dict[char] += 1
    
for char in s: 
    if non_repeating_char_dict[char] == 1:
        print(char)
        break
    
# group members by parity
parity_dict = defaultdict(list)
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    if num % 2 == 0:
        parity_dict["even"].append(num)
    else:
        parity_dict["odd"].append(num)
print(dict(parity_dict))

# group anagrams
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_dict = defaultdict(list)
groups = []
for word in words:
    group_dict[str(sorted(word))].append(word)
groups.append([val for val in dict(group_dict).values()])
print(groups)

# group indices by value

indices_values = [1, 2, 1, 3, 2, 1]
dict_indices = defaultdict(list)

for i in range(0, len(indices_values)):
    val = indices_values[i]
    dict_indices[val].append(i)
print(dict(dict_indices))

# invert a dictionary 

invert_dict = {"a": 1, "b": 2, "c": 1}
invert_dict_result = defaultdict(list)
for key, value in invert_dict.items():
    invert_dict_result[value].append(key)
print(dict(invert_dict_result))

# Two sum

nums = [2,7,11,15,2]
target = 9
two_sum_dict = dict()

for i in range(0, len(nums)):
    remaining = target - nums[i]
    if remaining in two_sum_dict:
        print([two_sum_dict[remaining], i])
    two_sum_dict[nums[i]] = i
print(two_sum_dict)

# most frequent elem

most_frequent_arr = [1, 3, 2, 3, 4, 3, 1]
mf_dict = defaultdict(int)
mf_set = set(most_frequent_arr)

for num in most_frequent_arr:
    mf_dict[num] += 1

print(max(mf_dict[elem] for elem in mf_set))