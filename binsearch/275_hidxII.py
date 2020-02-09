# Nathan Zhu Friday January 17th, 2020 2:45 pm Duderstadt Basement next to 376 OH doing proof of karatsuba algo.
# Leetcode 275 | medium | hard-ish
# Category: Binary Search
# The thinking is not exactly that easy for this one, but otherwise, this is a standard binary search.


def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    #       [0, 1, 3, 5, 6]
    #    idx 0  1  2  3  4
    #N - idx 5  4  3  2  1
    # We want to find the smallest point where N - idx >= citations[idx]
    # 
    # Is it possible for any cases to have N - idx < citations[idx] at all points?
    # A: Yes, suppose this: citations = [10, 10, 7]
    # We should return length of array in this case, which is 3, but the binary search should handle this.ArithmeticError
    #
    # What should ret be initialized to?
    # A: Ret should be initted to a  value that would be correct if N - mid > citations[mid] for all points in citations.
    #    Only way this is possible is if all the points in the array are 0.
    #  
    N = len(citations)
    ret = 0  # this is "REALLY" tricky
    l, r = 0, N - 1
    
    while l <= r:
        mid = (r - l) // 2 + l
        if N - mid <= citations[mid]:
            ret = N - mid
            r = mid - 1
        else: 
            l = mid + 1
    
    return ret