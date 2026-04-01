import math
avg_inp = [1, 2, 3, 4, 5]
k = 3


def maxSubarray(nums, k):
    max_sum = -math.inf
    local_sum = 0
    for i in range(0, len(nums)):
        local_sum += nums[i]

        if i >= k - 1:
            max_sum = max(max_sum, local_sum)
            local_sum -= nums[i - (k - 1)]
    return max_sum

max_subarray = maxSubarray(avg_inp, k)
print(max_subarray)

def minSubarray(nums, k):
    max_sum = math.inf
    local_sum = 0
    for i in range(0, len(nums)):
        local_sum += nums[i]

        if i >= k - 1:
            max_sum = min(max_sum, local_sum)
            local_sum -= nums[i - (k - 1)]
    return max_sum

min_subarray = minSubarray(avg_inp, k)
print(min_subarray)
