# Nathan Zhu May 4th, 2020 Pair programming with Austin. 
# Leetcode 378 | medium | damn this one had a cool soln.
# I didn't realize that given a number x, we can find the number of numbers <= x in
# O(M + N) time.  When you realize that, you can just do a binary search between max and min.
#

# Runtime is (M + N) * Log(max(arr) - min(arr))

def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    # runs in M + N time
    def count(target):
        R, C = len(matrix), len(matrix[0])
        r, c = R - 1, 0
        ret = 0
        
        while r >= 0 and c < C:
            while r >= 0 and matrix[r][c] > target:
                r -= 1
            ret += (r + 1)
            c += 1
        return ret
    
    R, C = len(matrix), len(matrix[0])
    left, right = float('inf'), float('-inf')
    for r in range(R):
        for c in range(C):
            left = min(matrix[r][c], left)
            right = max(matrix[r][c], right)
    
    # Note that there are many values x between min(arr) <= x <= max(arr)
    # s.t. there are k elements smaller or equal to x.  We need to find
    # the smallest value x for which this is true. This ensures that x is
    # inside the array as an actual number.
    ret = -1
    while left <= right:
        mid = (right - left) // 2 + left
        
        ct = count(mid)
        if ct < k:
            left = mid + 1
        elif ct >= k:
            ret = mid
            right = mid - 1
            
    return ret