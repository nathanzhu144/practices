

# Nathan Zhu May 2nd, 2020. Done during weekly conctest 182, placed top 400.  Amazing.
# Leetcode 1437 | medium | EZZ
# 
# This question was super easy.
#
# I finished the first 3 questions in the contest after spending ~29 min
# Q3 took me another 40ish min.  
# I originally wrote a N^2 soln and from intuition reduced it to O(N)
# with a sliding window and a monotonic queue.  I was so damn proud of myself
# for this one, like so damn proud.  This contest has been prob one of the highlights
# of 2020.
#
# Also, I crushed the hard one on this one with a "genius" idea from merging 
# k-sorted linked lists.  I was so impressed.

def kLengthApart(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    i = 0
    last_one = float('-inf')
    
    while i < len(nums):
        if nums[i] == 1:
            if i - last_one <= k: return False
            last_one = i
        i += 1
    return True