# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
# The intersection of two closed intervals is a set of real numbers that is either empty, or can be 
# represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# # 1. Sort both intervals by start
# # 2. 
# [1, 5] [6, 7] [10, 11]
# [4, 9]


def intervalIntersection(A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    ret = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        # A[i].start > B[j].end 
        # Case 1 no merge
        # [4, 5]  <- A[i]
        # [0, 3]  <- B[j]
        if A[i][0] > B[j][1]: j += 1
        # B[i].start > A[j].end 
        # Case 2 no merge
        # [0, 3]  <- A[i]
        # [4, 5]  <- B[j]
        elif B[j][0] > A[i][1]: i += 1
        # Case 3: Must have merge
        else:
            ret.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            # Now, which one do we increment?
            # We increment interval with earlier ending, or 
            # choose a random one with a tie.
            # Ex. 
            #   A = [3, 7]
            #   B = [5, 9]
            # We increment A's index, i++
            # 
            #   Ex. 
            #   A = [3, 7]
            #   B = [5, 6]
            # We increment B's index, j++
            if A[i][1] < B[j][1]: i += 1
            else: j += 1
    return ret
            
            
            