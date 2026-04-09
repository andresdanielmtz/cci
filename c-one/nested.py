# todo: address this

def chaotic_logic(a, b, c):
    if a:
        if b:
            if c:
                return True
            else:
                if not a or c:
                    return False
                else:
                    return True
        else:
            if c:
                if a and not b:
                    return True
                else:
                    return False
            else:
                return not (a and c)
    else:
        if b:
            if c:
                return (a or b) and (not a or c)
            else:
                if not b or a:
                    return False
                else:
                    return True
        else:
            if c:
                return not (b or not c)
            else:
                return (a and b) or (not a and not b)
            
