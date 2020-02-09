# Nathan Zhu Thurs Jan 29th, 2020 North Campus, Courtyards, 7:00 pm, about to go to Coco's 
# Redone     Mon Feb 3rd, 2020, SI 106 discussion.
# Leetcode 1060 | medium | tbh kinda hard
# Category: binsearch search.

def missingElement(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    # [4, 7, 9, 10]    3
    #  0  1  2  3
    #       
    # 3 - 2
    def num_missing(i):
        return nums[i] - nums[0] - i
    
    N = len(nums)
    
    # Two cases:
    # 1. missing element is bigger than list.
    #
    # k - num_missing > 0
    # 2. missing element is inside list.
    if k - num_missing(N - 1) > 0: return nums[-1] + k - num_missing(N - 1)
    
    # Find biggest one less than or equal to k.
    ret = -1
    left, right = 0, N - 1
    while left <= right:
        mid = (right - left) // 2 + left
        
        if num_missing(mid) < k:
            ret = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return k - num_missing(ret) + nums[ret] 