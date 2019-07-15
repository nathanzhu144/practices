#  Nathan Zhu 9:48 am, Amex building,
#  Leetcode 33 | medium | I think damn hard
#  
#  MESSING UP ONE TINY DETAIL WILL MESS UP THE ALGORITHM.
#  This is probably the most bug-prone code I've ever seen in the ~130 leetcode questions I've done so far.
#  I submitted literally 15 times when trying to debug this, and ran into more than 7 TLEs cause I messed up
#  the while loop somehow.  I highlighted all areas I think subtle bugs can occur.
# 
#  A lot of these bugs were a direct result of me not understanding the edge cases of the algorithm.
#
#  I'm legitimately scared of binary search, more than anything else.
#
#  NOTE: This is a case in which l <= r to break the while loop simplifies things.
#        I got it to work with l < r, but it was very ugly
#  NOTE: According to a random comment:
#        You use while (start <= end) if you are returning the match from inside the loop.
#        You use while (start < end) if you want to exit out of the loop first, and then use the result of start or end to return the match.

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    
    # The idea is simple.
    # If we do a binary search on a rotated array, there are 2 cases
    #   - mid and target are on same side of array
    #   - mid and target are on different sides of array
    #  
    # Ex. Suppose we have ...
    # 
    #    [4, 7, 9, 11, 1, 2]
    # 
    #    If our target is 2, we want our array to look like...
    # 
    #    [-inf, -inf, -inf, -inf, 1, 2]
    #
    #    If our target is 7, we wanr our array to look like...
    # 
    #    [4, 7, 9, 11, inf, inf]
    #
    #
    
    # NOTE: We use l <= r 
    #       Reason: On last iteration when l == r, mid == l == r.  If the comparator == target doesn't trigger, the
    #               item doesn't exist in the array, so we return -1 outside while loop.
    while l <= r:
        mid = (r - l) // 2 + l  # same as  mid = (l + r) / 2, but less chance of int overflow
        comparator = nums[mid]
        
        # We check to see if target and mid are on same side, if they are
        # we do a regular binary search. 
        # There's 1 possible bug here.
        # 1. It is WRONG to have nums[mid] > nums[0] and target > nums[0] instead of nums[mid] >= nums[0] and target >= nums[0]
        #    Target and mid being greater or EQUAL to nums[0] means that both are on the left side
        #    Ex. Supppose target is nums[0] and mid > nums[0].  In this case, both target and mid are on same side
        if nums[mid] < nums[0] and target < nums[0] or nums[mid] >= nums[0] and target >= nums[0]:
            comparator = nums[mid]
            
        else:
            # at this point we KNOW target and mid are on DIFFERENT SIDES
            # There's room for 2 major bugs here...
            # 1.  DO NOT USE MID TO COMPARE against nums[0], MID WILL CHANGE, AND WONT BE ACCURATE. 
            #     Use target to do the comparison against nums[0]
            #
            # 2. If target == nums[0], comparator should be set to float('inf'), do not forget this. 
            #    reason for this is that target is on left side of array in this case
            #
            #  If target is greater OR EQUAL to nums[0], target is on the left half, set mid to pos inf
            #  If target is less than nums[0], target is on right half, set mid to neg inf
            comparator = float('-inf') if target < nums[0] else float('inf')
                
        if comparator == target: return mid
        elif comparator < target: l = mid + 1
        elif comparator > target: r = mid - 1
    
    return -1