# Nathan Zhu 6:05 pm, Stockton, CA. June 30th, 2020.
# Leetcode 189 | easy | in-place is pretty hard
# Category: Misc tricks 



def rotate_not_in_place(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    N = len(nums)
    k %= N
    temp = nums[:]
    
    for i in range(N):
        nums[(i + k) % N] = temp[i]
        
def rotate_in_place(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # [1, 2, 3, 4, 5, 6, 7]
    #  0  1  2  3  4  5  6
    #
    #  4, 5, 6, 7, 1, 2, 3    k = 4
    #  4  5  6  7  1  2  3
    #  
    # left, right inclusive
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1

    N = len(nums)
    k %= N
    reverse(0, N - 1)
    reverse(0, k - 1)
    reverse(k, N - 1)