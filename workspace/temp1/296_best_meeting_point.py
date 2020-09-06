# Nathan Zhu May 28th, 2020
# Leetcode 296 | hard | kinda challenging 
# Category: Math

# There are two big conceptual leaps:
# 1. In 1D space, we get the minimial distance by taking the median of the points.
#    Ex. [1, 0, 0, 0, 1, 1]
#         0  1  2  3  4  5
#    Mean = (0 + 4 + 5) / 3 = 3
#    This gives us a minimal distance of 3 + 1 + 2 == 6
#    Median = 4
#    This give us a minimal distance of 4 + 0 + 1 = 5
#    
#    A "proof" of this is that assuming we are at the minimal points, in this example, and we move left.  Our distance to 0 decreases by 1,
#    but our distance to 4 & 5 increase by 1 too respectively for a net increase of 1.
#    Same with moving right
#
# 2. in 2D Space, we get the minimal distance by finding the 1D case in X and Y respectively.
#    This makes sense - there are no barriers, so we can never increase Y-distance by optimizing X-distance.
#    Therefore, closest is smallest of the two 1D cases.
# 
# # If grid is empty. problem is kinda invalid, so assume grid is not empty.
def minTotalDistance(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # behav not defined for len(arr) == 0
    def get_median(arr):
        arr.sort()
        N = len(arr)
        return arr[N // 2] if N % 2 == 1 else (arr[N // 2 - 1] + arr[N // 2]) / 2.0
    
    R, C = len(grid), len(grid[0])
    rows, cols = [], []
    for r in range(R):
        for c in range(C):
            if grid[r][c] != 0:
                rows.append(r)
                cols.append(c)
                
    medianr, medianc = get_median(rows), get_median(cols)
    ret = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c]:
                ret += abs(r - medianr) + abs(c - medianc)
    return int(ret)