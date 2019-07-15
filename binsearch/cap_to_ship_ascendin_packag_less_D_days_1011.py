#  Nathan Zhu, Wed June 26th, 3:29 pm
#  Leetcode 1011 | Medium | I think hard without insight, but not bad with insignt

def shipWithinDays(self, weights, D):
    """
    :type weights: List[int]
    :type D: int
    :rtype: int
    """
    lo, hi = max(weights), sum(weights)
    
    # Wed June 26th, 3:29 pm
    # The very first insight is that it must be true that total
    # capacity >= maximum weight and total capacity is <= sum(weights)
    #
    # Second, we are trying to find the minimum capacity s.t. we can 
    # fulfill in D days.  Somewhere in between max(weights), sum(weights)
    # exists a capacity C such that we can furfill in <= D days, but
    # with a capacity C - 1, we cannot furfill in <= D days.
    #
    # So, we do a binary search. Given that capacity, we see whether the number
    # of days is <= or D.  I
    # . 1. If it is <= D, it could be that element, but we could potentially 
    #      minimize capacity by using more days, so we set:
    #          high = mid
    #   2. If it is > D, it cannot be that element, we must increase capacity
    #      to reduce number of days it takes to ship everything. 
    #          low = mid + 1
    while lo != hi:
        mid = (lo + hi) // 2
        tot, days = 0, 1
        
        # We find number of days it takes to ship everything
        for wt in weights:
            # we need to put new item for tomorrow
            if wt + tot > mid:
                days += 1
                tot = wt
            # we can fit new item for today
            else:
                tot += wt
        # Situation 1
        if days <= D: hi = mid
        # Situation 2
        else: lo = mid + 1
            
    return lo