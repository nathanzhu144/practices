# Nathan Zhu 1:48 am January 3rd, 2019, just got back from Monterey yesterday!
# Leetcode 581 | easy | I have done hards that were slightly easier.
# Category: Sliding window / misc tricks

def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Step 1: 
    # Find the first position s.t. nums is no longer ascending.  We call this idx i 
    # Find the last position s.t. nums is no longer ascending.   We call this idx j
    #
    #   2 6 4 8 10 9 15
    #     ^        ^
    #     i        j
    #
    # However, while the sequence before i and after j are sorted, sorting between i and j will not 
    # guarantee the whole array is sorted.  We need move i to the left until it is <= min element in array between i and j
    # We need to move j to the right until it is >= max element in array between i and j
    #   2 6 4 8 10 9 15
    #   ^            ^
    #   i            j
    #
#    ix 0 1 2 3  4 5 6
    
    
    N = len(nums)
    i, j = 0, N - 1
    while i + 1 < N and nums[i] <= nums[i + 1]: i += 1
    while j - 1 >= 0 and nums[j - 1] <= nums[j]: j -= 1
        
    if j <= i: return 0
    
    small, big = float('inf'), float('-inf')
    for n in range(i, j + 1):
        small = min(nums[n], small)
        big = max(nums[n], big)
        
    while i >= 0 and nums[i] > small: i -= 1
    while j <= N - 1 and nums[j] < big: j += 1
        
    
    return j - i - 1
        

if __name__ == "__main__":
    print(findUnsortedSubarray([2, 1]))