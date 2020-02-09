# Nathan Zhu Jan 26th, 2020 10:25 am 3rd Floor Ugli
# Leetcode 287 | medium | hard man
# Category: Linked list, tortise hare algorithm
# Damn this problem is mean, but damn it is cool.
# See notes on it.

def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1: return -1
    
    fast, slow = nums[nums[0]], nums[0]
    
    while fast != slow:
        fast = nums[nums[fast]]
        slow = nums[slow]
        
    fast = 0
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
        
    return slow