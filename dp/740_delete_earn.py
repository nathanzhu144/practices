# Nathan Zhu 9:39 pm January 17th, 2019 Foundry Lofts
# Leetcode 740 | medium | yeah not bad
# Category: DP (like house robber)
# Runtime: NlogN
# Note that if nums range is bounded, we can do a bucket sort and do this in O(N) time


def deleteAndEarn(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    
    # arr represents all the unique ints in the array in a sorted inc order
    arr = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            arr.append(nums[i])
            
    c = collections.Counter(nums)
    N = len(arr)
    table = dict()
    
    def helper(arr, i):
        if i >= len(arr): return 0
        if i in table: return table[i]
        
        # If the next greater element is more than 1 greater, we definitely choose this element
        if i + 1 < len(arr) and arr[i + 1] > arr[i] + 1:
            table[i] = arr[i] * c[arr[i]] + helper(arr, i + 1)
        # Else, we choose (similar to house robber)
        else:
            table[i] = max(arr[i] * c[arr[i]] + helper(arr, i + 2), helper(arr, i + 1))
        return table[i]
    
    return helper(arr, 0)
    