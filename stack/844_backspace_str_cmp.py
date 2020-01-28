# Nathan Zhu Jan 27th, 2019 11:00 am SI 106 class.
# Leetcode 844 | easy | EZ
# Category: Stack.

def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    st1, st2 = [], []
    
    for c in S:
        if c == "#" and st1: st1.pop()
        elif c != "#": st1.append(c)
            
    for c in T:
        if c == "#" and st2: st2.pop()
        elif c != "#": st2.append(c)
            
    return "".join(st1) == "".join(st2)