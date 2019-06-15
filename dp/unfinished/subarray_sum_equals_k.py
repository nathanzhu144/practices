
#  This is a n^3 soln to a n^2 soln.  See num_subarrays_in_boundary
def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Note, whats the implication of negatives
    
    returned = 0
    potentials = dict()   #maps (i, j) to -> sum of nums[i] to nums [j]
    
    for i in range(len(nums)):
        potentials[(i, i)] = nums[i]
        if nums[i] == k:
            returned += 1
            
    for i in range(len(nums) - 1):
        potentials[(i, i + 1)] = nums[i] + nums[i+1]
        if nums[i] + nums[i + 1] == k:
            returned += 1
            
    for j in range(2, len(nums)):
        for i in range(j - 1):
            total_sum = nums[i] + potentials[(i + 1, j - 1)] + nums[j]
            potentials[(i, j)] = total_sum
                
            if total_sum == k:
                returned += 1
    
    return returned