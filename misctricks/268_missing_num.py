# Nathan Zhu Jan 5th, 2020.  SI 106, We have an exam tomorrow, lol.
# Leetcode 268 | easy | easy
# Category: Misc tricks
# You can do an XOR, too.
# Also, this can overflow in some languages, but I think this is a cool soln.
# This works because nums are between 0 -> N, and one is missing.

def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 0 1
    # 
    N = len(nums)
    return N * (N + 1) // 2 - sum(nums)