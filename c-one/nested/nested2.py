'''
outputs when its false

1,0,1
0,1,1
0,1,0
'''

def chaotic(a, b, c):
    if (a and not b and c) or (not a and b and c) or (not a and b and not c):
        return False
    return True