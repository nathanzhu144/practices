# Nathan Zhu Done on December 23rd, 2019 11:00 am Waiting in line at ski resort for special ticket, someone seemed to reissue my ticket. 
#                 typed up on Dec 26th, 2019.
# Leetcode 89 | medium | medium
# Category: Bits, misc-tricks.
# 


def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """
    
    # 0 0 0
    # 0 0 1
    # 0 1 1
    # 0 1 0
    # 1 1 0
    # 1 1 1 
    # 1 0 1
    # 1 0 0
    
    # ...
    
    # Rule for each new power, we reverse the sequence, and flip 1st bit to one.  
    # This can be done by adding a power of 2.
    #
    
    def helper(n):
        new = ret[:]
        
        # Going backwards, to reverse the sequence.
        for i in range(len(new) - 1, -1, -1):
            # adding a power of 2 to flip front bit to one
            new.append(2 ** n + new[i])

        return new
    
    ret = [0]

    for i in range(n):
        ret = helper(i)
    return ret
    