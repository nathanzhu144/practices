# Nathan Zhu May 18th, 2020, 7:05 pm, Broke top 200 last week, got exactly 188 briefly, but went down to position 400 because I had 4 stupid mistakes.  
# Leetcode 1388  | hard | not that bad, but kinda hard
# Category: DP
# This is basically the same as house robber II.
# However, there are some slight differences.  
#
# 1. Similar to last house robber II, we EITHER TAKE THE FIRST SLICE OR LAST SLICE BUT NOT BOTH.
#    Therefore, we can break the dependency by calculating the max of the function on two possible arrays,
#    the array including the first element, but not the last element or the array including the last element
#    but not the first element.
#  
# 2. Unlike house robber II, we can only take N // 3 slices.  I had the bug where I was taking more than N // 3 slices,
#    and we need to do a 2d dp instead of a 1d dp.  This is in contrast to house robber II 
def maxSizeSlices(self, arr):
    """
    :type slices: List[int]
    :rtype: int
    """
    
    # arr - array
    # i   - position in array
    # k   - slices we can take left
    # table - dp
    def helper(arr, i, k, table):
        key = (i, k)
        if key in table: return table[key]
        if k < 0: return float('-inf')
        if i >= len(arr): return 0

        table[key] = max(helper(arr, i + 1, k, table), helper(arr, i + 2, k - 1, table) + arr[i])
        return table[key]
    
    N = len(arr)
    ret = max(helper(arr[1:], 0, N // 3, dict()), helper(arr[:-1], 0, N // 3, dict()))
    return max(ret, 0)