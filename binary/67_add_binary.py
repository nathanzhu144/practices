# Nathan Zhu April 7th, 2020. 12:01 am.  Foundry Lofts, COVID-19
# Leetcode 67 | easy | easy
# Category; binary, bits
# 



def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    f1, f2 = a[::-1], b[::-1]
    N1, N2 = len(f1), len(f2)
    i1, i2 = 0, 0
    
    
    ret = []
    carry = 0
    
    while i1 < len(f1) or i2 < len(f2):
        val1, val2 = 0, 0
        if i1 < N1: val1 = int(f1[i1])
        if i2 < N2: val2 = int(f2[i2])
            
        curr = carry + val1 + val2
        carry = curr // 2
        ret.append(curr % 2)
        i1 += 1
        i2 += 1
        
    if carry: ret.append(1)
    ret = map(str, ret)
    return "".join(ret[::-1])