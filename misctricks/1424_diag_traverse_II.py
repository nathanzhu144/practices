# Nathan Zhu April 28th, 2020  376 exam in a few days, Stockton, California  Wekly contest 181
# Leetcode 1424 | medium | not bad
# Category: Misc tricks
# I like liked this one.


import collections

# More efficient, same big-O, but runs a lot faster.
def findDiagonalOrder(nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    R = len(nums)
    if not R: return []
    table = collections.defaultdict(list)
    max_bucket = 0
    for r in range(R):
        for c in range(len(nums[r])):
            table[r + c].append(nums[r][c])
            max_bucket = max(r + c, max_bucket)

    ret = []
    for bucket in range(max_bucket + 1):
        if bucket in table: ret.extend(table[bucket][::-1])
    return ret

# More efficient, same big-O, but runs a bit slower
def findDiagonalOrderInefficient(nums):
    r, c = 1, -1
    R = len(nums)
    if not R: return []
    next_row = 2
    
    target = sum([len(item) for item in nums])
    ret = []
    
    while True:
        r, c = r - 1, c + 1
        if 0 <= r < R and 0 <= c < len(nums[r]):
            ret.append(nums[r][c])
        
        if r < 0:
            r, c = next_row, -1
            next_row += 1
        if len(ret) == target: return ret
        
    return []