# Nathan Zhu Jan 24th, 2020 11:05 am Duderstadt, trying to do this in Hershal's grad algo discussion
# Leetcode 1326 | hard | yeah hard
# This greedy soln is kinda unintuitive.
#
# Idea is that you can reduce this problem to jump game II.
# 
def minTaps(n, ranges):
    """
    :type n: int
    :type ranges: List[int]
    :rtype: int
    """
    
    water = [0 for i in range(n + 1)]
    for i in range(n + 1):
        left = max(0, i - ranges[i])
        right = min(n, i + ranges[i])
        water[left] = max(right - left, water[left])
        
    start, end = 0, 0
    ret = 0
    while end < n:
        ret += 1
        start, end = end, max(water[i] + i for i in range(start, end + 1))
        if start == end: return -1
    return ret

print(minTaps(8, [4,0,0,0,0,0,0,0,4]))
print(minTaps(0, [1]))