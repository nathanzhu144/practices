# Nahan Zhu May 23rd, 2020 saturday, weekly contest
# Leetcode 1458 | hard | yeah an easier hard
# Category: DP
# Similar to LCS, LiS, LPS questions

def maxDotProduct(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    
    
    R, C = len(nums1), len(nums2)
    
    table = [[0 for c in range(C + 1)] for r in range(R + 1)]
    
    ret = float('-inf')
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            table[r][c] = max(0, table[r - 1][c - 1]) + nums1[r - 1] * nums2[c - 1]
            table[r][c] = max(table[r - 1][c], table[r][c - 1], table[r][c])
            if nums1[r - 1] * nums2[c - 1] < 0: ret = max(ret, nums1[r - 1] * nums2[c - 1])
            else: ret = max(ret, table[r][c])
    #print(table)
    return ret