s = "asdgbbbasd"
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

