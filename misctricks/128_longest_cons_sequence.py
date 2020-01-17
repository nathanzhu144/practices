# Nathan Zhu Dec 26th, 2019 9:54 pm, Napa Valley California
# Leetcode 128 | hard | cool one man
# Category: Misc tricks
#
# The trick is amazing.
# We want to find the longest increasing cons sequence like 
#   6, 7, 8, 9
# in O(N) time.
#
# We first put all the numbers into a set.
# Then, we iterate thru all the numbers.  If number - 1 doesn't exist 
# in the set, it is the beginning of an increasing sequence.
# We incremenet this number until we cannot find it in the set, and track the path size.
# 
# 
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = set(nums)
    
    ret = 0
    for num in nums:
        # ensuring this is beginning of a cons increasing sequence
        if num - 1 not in nums:
            nextnum = num
            while nextnum + 1 in nums:
                nextnum += 1
            
            # at this point, nextnum is largest number in sequence
            # therefore length of this sequence is largest num - first num + 1
            ret = max(nextnum - num + 1, ret)
            
    return ret