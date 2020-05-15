# Nathan Zhu Feb 14th, 2020.  We went to Aventura today for Valentine's.  Good times.
# Leetcode 496 | easy | medium
# Category: monotonic stack

def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    stack = []
    ret = []
    table = dict()
    for i, num in enumerate(nums2):
        while stack and stack[-1] < nums2[i]:
            table[stack[-1]] = num
            stack.pop()
        stack.append(num)
        
    while stack:
        table[stack.pop()] = -1
        
    for num in nums1:
        ret.append(table[num])
        
    return ret