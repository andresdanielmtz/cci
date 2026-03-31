nums = [1,2,3,4]
res = [nums[0]]

for i in range(1, len(nums)):

    curr = nums[i] + res[i - 1] # the current one + the previous sum (res[i-1])
    print("i: ",i, "nums[i]", nums[i], "curr", curr)
    res.append(curr)
print("res", res)