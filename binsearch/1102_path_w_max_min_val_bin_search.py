# Nathan Zhu May 9th, 2020. Did leetcode bootcamp with meera and shazeen today.
# Leetcode 1102 | medium | damn cool
# Category: Binary search
#
# This can also be done with Union find and djikstra in same runtime, MNLogMN
# 

# Done w binary search
def maximumMinimumPath(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    
    # We can check to see if a path goes from start to end with minimum square being k in
    # M * N time.
    #
    # We can find all squares and sort them in (MN)log(MN) time by value.
    # 
    # Then, since if there exists a path between start and end with minimum square k, there 
    # also must exist one with k - 1, we can do a binary search on the values set, and 
    # find the largest square value for which a path is still possible.
    #
    # Overall (MN)log(MN), same as djikstra runtime
    
    def dfs(x):
        visited = set()
        def helper(r, c, x):
            R, C = len(A), len(A[0])
            if r == R - 1 and c == C - 1: return True
            
            for newr, newc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= r < R and 0 <= c < C and (newr, newc) not in visited and A[r][c] >= x:
                    visited.add((newr, newc))
                    if helper(newr, newc, x): return True
            return False
        return helper(0, 0, x)
    
    if not A or not len(A[0]): return -1
    R, C = len(A), len(A[0])
    ceiling = min(A[0][0], A[R - 1][C - 1])
    search = set()
    for r in range(R):
        for c in range(C):
            if A[r][c] <= ceiling: search.add(A[r][c])
    
    search = sorted(list(search))
    left, right = 0, len(search) - 1
    ret = -1
    while left <= right:
        mid = (right - left) // 2 + left
        if dfs(search[mid]):
            ret = mid
            left = mid + 1
        else:
            right = mid - 1
    return search[ret]