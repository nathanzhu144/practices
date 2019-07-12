

def can_partition_k_subsets(nums, k):

    def helper(nums, k, curr_sum, target, index):
        if k == 1: return True
        if index >= len(nums): return False
        
        ret = False
        for i in range(index, len(nums)):
            if curr_sum + nums[i] < target:
                # This is wrong cause we have to use this index.  # if we want to eitehr use or 
                # not use thise index, this could actually work
                #ret = ret or helper(nums, k, curr_sum + nums[i], target, i + 1)
                curr_sum += nums[i]
            if curr_sum + nums[i] == target:
                ret = ret or helper(nums, k - 1, 0, target, i + 1)
            else:
                pass
                # do nothing, we cannot add this to curr_sum
        return ret
    if sum(nums) % k != 0: return False
    return helper(nums, k, 0, sum(nums) // k, 0)

if __name__ == "__main__":
    print(can_partition_k_subsets([4,3,2,3,5,2,1], 4))