# Nathan Zhu Leetcode 10:13 pm Foundry Lofts Jan 17th, 2020
# Leetcode 1047 | easy | EZ
# Category: Stack

def removeDuplicates(self, S):
    """
    :type S: str
    :rtype: str
    """
    ret = []
    for c in S:
        if len(ret) > 0 and ret[-1] == c:
            ret.pop()
        else:
            ret.append(c)
            
    return "".join(ret)