# Nathan Zhu March 19th, 2020 10:12 pm
# Leetcode 503 | medium | kinda hard tbh
# Category: Monotonic stack


def nextGreaterElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    stack = []
    N = len(nums)
    ret = [-1] * N
    
    for i in range(N * 2 - 1, -1, -1):
        ridx = i % N
        while stack and nums[ridx] >= nums[stack[-1]]:
            stack.pop()
            
        
        if not stack: ret[ridx] = -1
        else: ret[ridx] = stack[-1]
        stack.append(ridx)
            
    return [nums[i] if i >= 0 else - 1 for i in ret]