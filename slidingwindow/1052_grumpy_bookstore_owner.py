# Nathan Zhu 10:23 pm December 27th, 2019 Just got back from Napa Valley, hot air ballooning and napa valley today
# Leetcode 1052 | medium | EZ
# Category: Sliding window

def maxSatisfied(customers, grumpy, X):
    """
    :type customers: List[int]
    :type grumpy: List[int]
    :type X: int
    :rtype: int
    """
    # Find number of customers definitely satisfied without using technique
    # Change the customers in non-grumpy minutes to 0 for easier processong later on
    ret = 0
    for i in range(len(customers)):
        if grumpy[i] == 0: 
            ret += customers[i]
            customers[i] = 0
    
    # A B C D
    # 0 1 2 3
    #        Len == 3
    currmax = 0
    curr = 0
    for i in range(len(customers)):
        curr += customers[i]
        if i >= X: curr -= customers[i - X]
        currmax = max(curr, currmax)
        
    return currmax + ret