# Nathan Zhu, 12/18/2021, Stockton, CA.  12:59 pm.  Going to speak at Neil's wedding next week!
# Leetcode 902 | hard | kinda challenging
# Category: Math, specifically counting



def atMostNGivenDigitSet(digits, n):
    """
    :type digits: List[str]
    :type n: int
    :rtype: int
    """
    ret = 0
    n = str(n)
    len_n = len(n)
    
    # all numbers of 1 length shorter than n can use all the
    # digits per place
    for i in range(1, len_n):
        ret += len(digits) ** i
        
    for i in range(len_n - 1, -1, -1):
        curr_has_prefix = False
        for d in digits:
            if d < n[len_n - i - 1]:
                ret += len(digits) ** i
            if d == n[len_n - i - 1]:
                curr_has_prefix = True
        
        # case where one of the digits composing n is not in our digits set
        if not curr_has_prefix:
            return ret
        
    return ret + 1