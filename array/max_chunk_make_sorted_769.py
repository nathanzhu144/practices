# Nathan Zhu Amex Building, 200 Vessey Street, NY
# Leetcode 769 | medium | I think medium is fair
# Wednesday 5:00 pm June 26th, 2019

# Leet

def maxChunksToSorted(self, arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    ret = 0
    
    sorted_arr = sorted(arr)
    
    # So, this question is kinda confusing. 
    # The idea is what is the maximum number of segments you can
    # split an array, so that when you sort each of the segments, you
    # can just concatenate them to make a sorted array
    #
    # So, the generalized NlogN approach is to keep 2 arrays
    # 1. sorted arr
    # 2. an arr of maximum of arr at that index
    #
    # We iterate through all the indices of arr, and 
    # if max_arr[i] == sorted_arr[i], at this point,
    # all numbers to left are <= the arr[index] at this point.
    # all numbers to right are >=  the arr[index] at this point
    # Therefore, we can increment the split
    # 
    
    
    curr_max = float('-inf')
    max_arr = []
    for i in arr:
        curr_max = max(i, curr_max)
        max_arr.append(curr_max)
        
    for i in range(len(arr)):
        if max_arr[i] == sorted_arr[i]:
            ret += 1
    return ret
            