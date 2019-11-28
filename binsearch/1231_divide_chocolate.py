# Nathan Zhu Wed Nov 27th, 2019, 8:38 pm. At Johnny's house and we are watching the good place w johnny's mom.
# Leetcode 1231 | hard | yeah pretty hard in some ways.
# Category: Greedy / Binary search.
# 
# 

def maximizeSweetness(sweetness, K):
    """
    :type sweetness: List[int]
    :type K: int
    :rtype: int
    """
    
    def helper(sweetness, max_subarr_sum, K):
        curr, k = 0, 0
        for i in range(len(sweetness)):
            curr += sweetness[i]
            if curr > max_subarr_sum:
                curr = 0
                k += 1
            if k > K: return False
            
        return True
    
    low, high = min(sweetness), sum(sweetness)
    
    while low < high:
        mid = (high - low) // 2 + low
        if helper(sweetness, mid, K):
            high = mid
        else:
            low = mid + 1
            
    return low
            