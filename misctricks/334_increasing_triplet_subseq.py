# Nathan Zhu Jan 7th, 2020. Sitting in Living room of Foundry.  
# Leetcode 334 | medium | kind hard lool
# Category: Misc tricks
#
# A really naive soln is N^3.
#
# A naive soln could do LiS, and find if there's a subseq of at least 3.
# However, this would be N^2 time.  
# 
# A cool soln can do this in O(N) time, O(1) space


def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    small, big = float('inf'), float('inf')
    
    for num in nums:
        if num <= small:
            small = num
        elif num <= big:
            big = num
        else:
            return True
        
    return False