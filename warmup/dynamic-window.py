import math

example = "asdgbbbasd"

"""
Dynamic sliding window
"""

def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        curr_length = right - left + 1
        max_length = max(max_length, curr_length)

    return max_length


"""
Fixed sliding window
"""


def maxSubarray(arr, k):
    max_sum = -math.inf
    local_sum = 0
    for i in range(0, len(arr)):
        local_sum += arr[i]

        if i >= k - 1: 
            max_sum = max(max_sum, local_sum) # calculate max
            local_sum -= arr[i - (k - 1)] # remove the last item to add the new one
    return max_sum
