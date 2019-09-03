# Nathan Zhu August 12th, 2019, Stockton CA, Mnday 1:51 am, PST, first leetcode prob back home
# Leetcode 41 | hard | hard if you don't know the trick
# Category: Misc tricks


def first_missing_pos_nlogn(nums):
    arr = sorted(nums)
    ret = 1
    for num in arr:
        # num == ret deals with duplicate elements
        if num == ret: ret += 1
    return ret

# O(N) soln
def first_missing_pos(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 
    # Observations:
    #  - First missing positive is in range [1, len(nums) + 1] inclusive
    #    This is essential.
    # Approaches:
    # Naive Nlogn approach
    # 
    # 1. Sort whole array
    # 2. going from idx1 to end of array, return first array element 
    #    not equal to its index
    # 3. If none returns are triggered, return len(nums) + 1
    #
    #
    # 
    # Observations:
    # We know that first missing positive is len(nums) + 1 if first
    # missing positive is not in range [1, len(nums)].  Therefore,
    # ALL numbers outside this range are not useful, and can be
    # set to 0 (IMPORTANT for algorithm to work properly later)
    # 
    # What's an O(N) approach to find first missing positive?
    #
    # What if we used the array index as the hash to restore the
    # frequency of each number?
    #
    nums.append(0)
    
    for i in range(len(nums)):
        if nums[i] < 0 or nums[i] >= len(nums): nums[i] = 0
            
    for i in range(len(nums)):
        nums[nums[i] % len(nums)] += len(nums)
        
    for i in range(len(nums)):
        if nums[i] // len(nums) == 0: return i
    return len(nums)