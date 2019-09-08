# Nathan Zhu Completed September 6, 2019 5:43 PM
# Leetcode 88 | easy | EZ
# Category: array
# 
# Microsoft- Online Assessment
# Your interview score of 5.90/10 beats 58% of all users.


# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    num1idx, num2idx = m - 1, n - 1
    
    while num1idx >= 0 and num2idx >= 0:
        if nums1[num1idx] > nums2[num2idx]:
            nums1[num1idx + num2idx + 1] = nums1[num1idx]
            num1idx -= 1
        else:
            nums1[num1idx + num2idx + 1] = nums2[num2idx]
            num2idx -= 1
    
    while num2idx >= 0:
        nums1[num2idx] = nums2[num2idx]
        num2idx -= 1