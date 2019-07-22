#  Nathan Zhu 8:06 am, Amex tower, 200 Vessey Street, 36th floor, been 5 hours since I was at the office now I'm back
#  Leetcode 852 | easy | I think easy, for a bin search question, was hard when I did it two days ago
#
# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# 
# The comparison A[i] < A[i+1] in a mountain array looks like [True, True, True, #..., #True, False, False, ..., False]: 1 or more boolean Trues, followed by 1 or # #more #boolean False
def peakIndexInMountainArray(A):
    """
    :type A: List[int]
    :rtype: int
    """
    l, r = 0, len(A) - 1
    
    # When l == r, we should have mountain array element
    while l != r:
        mid = (l + r) / 2
        
        # believe mid + 1 should always be in range
        # mountain array ele cannot be last element
        if A[mid] < A[mid + 1]:
            l = mid + 1
        else:
            r = mid
    
    return l