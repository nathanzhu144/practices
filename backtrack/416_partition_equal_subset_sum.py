#  Nathan Zhu Amex 36th floor, 7:47 pm, Monday July 1st, 2019
#  Leetcode 416 | medium | med
#  Can we partition a set of POSITIVE INTEGERS into two equal sets?
#  
#  This is same as coin-change problem, but our target is sum(coins) // 2.
#  and we cannot re-use coins.


def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def helper(nums, index, target, mem):
        key = (index, target)
        if key in mem: return mem[key]
        
        if target < 0 or index < 0: return False
        if target == 0: return True
        
        mem[key] = helper(nums, index - 1, target, mem) or \
                    helper(nums, index - 1, target - nums[index], mem)
        return mem[key]
    
    if sum(nums) % 2 != 0: return False
    return helper(nums, len(nums) - 1, sum(nums) / 2, dict())

if __name__ == "__main__":
    print(canPartition([1, 2, 5]))