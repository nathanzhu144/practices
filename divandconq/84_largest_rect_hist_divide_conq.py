# Nathan Zhu March 16th, 2020.  Foundry Lofts during coronavirus quarantine.
# Leetcode 84 | hard | hard
# Category: Divide and conq, stack (this impl does former)
#
# Intuition: Largest rectangle in a histogram either includes the smallest bar or does not include
#            the smallest bar.  So, we can do a divide and conq on 3 cases:
#
#            1. small bar height * whole length of array in this recursive call
#            2. problem(subarray left of shortest bar)
#            3. problem(subarray right of shortest bar)
# 
# Worst case N^2 when array looks like [1, 2, 3 7, 9] or [102, 23, 11, 10, 2]
# Average case is NLogN, like quicksort.
#
def largest_rect_area_dq(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # Gets the idx of the minimum el of the array.
    def get_min_idx(arr):
        idx, curr = -1, float('inf')
        for i, num in enumerate(arr):
            if num < curr:
                idx = i
                curr = num
        return idx
    
    # Actual recursive function
    def helper(arr):
        # Base cases:
        # 1. Empty array has an area of 0.
        # 2. Single bar has an area of the height of that bar
        if not arr: return 0
        if len(arr) == 1: return arr[0]
        idx = get_min_idx(arr)
        return max(helper(arr[:idx]), helper(arr[idx + 1:]), arr[idx] * len(arr))
    
    return helper(heights)
    
            
if __name__ == "__main__":
    pass