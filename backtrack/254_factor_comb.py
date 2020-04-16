# Nathan Zhu April 2nd, 2020. Foundry Lofts, Final week.  COVID-19
# Leetcode 254 | medium | medium
# Category: Backtracking
# 
# The smart part of this impl is being able to avoid repeats by passing in a numerical floor.
def getFactors(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """

    
    ret = []
    # 24
    # 2 12
    #    2 2 6
    #     2 2 2 3
    # 2 3 4
    # 3 8
    # 4 6
    # 
    # 
    #   
    
    # Represents smallest number we can divide by.
    # Stack holds next number we will attempt to break up.
    # 
    # the idea is to iteratively divide the last number in the factor combo into smaller numbers
    # [12] ---divide 12 by 2---> [2, 6]  ---divide 6 by 2---> [2, 2, 3] ---3 cannot divide 2 so done---
    # [12] ---divide 12 by 3---> [3, 4] (---divide 4 by 2---> [3, 2, 2])*
    # to fix the issue of duplicates (* above) we pass the starting number for the factor search
    #  so if you've divided by 2, next try dividing by 2 or higher (hence 2, 2, 3)
    #  but if you now divide by 3, start the next division at 3
    # why stop when i*i=num? because any number K>sqrt(num) will have num/K<K which is duplicative
    def helper(i, stack):
        num = stack.pop()
        while i * i <= num:
            if num % i == 0:
                div = num / i
                ret.append(stack + [i, div])
                helper(i, stack + [i, div])
            i += 1
            
    helper(2, [n])
    return ret