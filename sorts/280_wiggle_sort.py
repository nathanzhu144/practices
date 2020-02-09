 # Nathan Zhu Jan 31st, 2020, Julie is mumbling her presentation rn.  2nd floor Duderstadt.
 # Leetcode 280 | medium | annoying
 # Category: sorts
 # I don't like wiggle sorts that much.
 #    
    
def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    for i in range(0, len(nums), 2):
        nums[i:i + 3] = sorted(nums[i:i+3])
        nums[i + 1: i + 3] = nums[i + 2: i: -1]

if __name__ == "__main__":
    print(wiggleSort([3,4, 5,2,1,6,4, 7]))