# Nathan Zhu August 2nd, 2019, 11:00 am, with Johnny
# Leetcode 1155 | medium | medium
# Category: DP

def numRollsToTarget(d, f, target):
    """
    :type d: int
    :type f: int
    :type target: int
    :rtype: int
    """
    table = dict()
    self.constant = 10 ** 9 + 7
    
    def helper(numdice, target, faces):
        key = (numdice, target)
        if key in table: return table[key]
        
        if numdice == 0 or target == 0: return numdice == 0 and target == 0
        
        ret = 0
        for i in range(1, faces + 1):
            ret += helper(numdice - 1, target - i, faces)
            
        table[key] = ret % self.constant
        return table[key]
    
    
    return helper(d, target, f)

