# Nathan Zhu 10/16/2021, Bucktown, Chicago.  10:23 am
# Leetcode 453 | medium | kinda challenging to think of
# Category: Misc tricks.


def minMoves(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # Example: 
    # [1, 2, 3]
        #
        # #
    # # #
    
        # #
    # # #
    # # #
    
        #
    # # #
    # # #
    # # #
    
    # # #
    # # # 
    # # #
    # # #
    
    # We don't care about the absolute value of the final numbers - we 
    # care about the difference between them.  
    #
    # Adding 1 to n - 1 elements is analagous to subtracting 1 from one
    # element.
    #
    # We can rephrase it as subtracting one until all elements are the same 
    # as minimum element.
    return sum(nums) - min(nums) * len(nums)