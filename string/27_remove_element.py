# Nathan Zhu Wednesday September 11th, 2019 12:54 pm
# Leetcode 27 | easy | EZ
# Category: string
#
# Given an array nums and a value val, remove all instances of that value in-place and 
# return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying the input 
# array in-place with O(1) extra memory.

# Increment left pointer only when arr[i] != val, then write to left ptr
def removeElement(arr, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    left = 0
    
    for i in range(len(arr)):
        if arr[i] != val:
            arr[left] = arr[i]
            left += 1
            
    
    return left