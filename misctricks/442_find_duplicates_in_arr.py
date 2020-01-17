# Nathan Zhu Tuesday December 31st, 2019 11:36 pm
# Leetcode 442 | medium | medium
# Category: misc tricks
#
# We take advantage of the fact that all numbers in nums are from 1 <= n <= N, and use the array as a hash table, modifying it.

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ret = []
    
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] < 0: 
            ret.append(abs(nums[i]))
        else: 
            nums[abs(nums[i]) - 1] *= -1
            
    return ret

if __name__ == "__main__":
    print(findDuplicates([4, 3, 3, 2, 10, 2]))