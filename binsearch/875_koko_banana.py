# Nathan Zhu 200 Vessey Street, New Yotk, June 26th, 6:30 pm
# Leetcode_875 | medium | idea is easy after seeing leetcode 1011
#
# NOTE: Since are always flooring (lo + high) // 2, medium is floor of average of high and low
#       Therefore, when we assign to high, high is always decreasing.  It will only stop decreasing
#       when lo == high, but loop will break before then.
#
#       so, I had a correct soln at first, but I kept subtracting k bananas for each pile
#       a bunch of times before moving onto next index, was too slow for large inputs.
#
#       Using list comprehension, we can do it in a more concise manner
#
#
# The variable we need to do binary search on is K, the number of bananas that Koko can eat before guards come
# So, we are trying to find a minimum K such that all banansa will be gone before guards come back.
# Essentially, once you figure out that "able to finish by eating K banans per hour before guards come back"
# is a TRUE or FALSE statement, you can begin doing bin search on K

def minEatingSpeed(piles, H):
    """
    :type piles: List[int]
    :type H: int
    :rtype: int
    """
    lo, high = 1, max(piles)
    
    while lo != high:
        # med is num bananas per hour
        med = (high - lo) // 2 + lo    
        # LOL THIS LINE TOOK LIKE 10 LINES BEFORE.
        # if we manage to eat all bananas in array within H hours. we see
        # if it is possible to find a lower value
        if sum((pile + med - 1) / med for pile in piles) <= H: high = med
        # we aren't eating bananas fast enough
        else: lo = med + 1
    return lo