from collections import Counter

s1 = "asdasdasdasd"
s2 = "asd"

# return true if s2 contains a permutation of s1

def isPermutation(s1, s2):
    k = len(s2)
    window = []
    for i in range(k, len(s1)):
        window.append(s1[i])
        
        if i >= k - 1:
            window.pop(i - (k - 1))
        print(window)
    
isPermutation(s1, s2)