
#  Nathan Zhu, Amex Tower, New York, Sunday June 23rd, 2019 36th floor
#  I'm surpried that this isn't a leetcode easy.  
#
#  Figuring out what a max binary tree took longer than anything else, honestly.
#  
#  The idea is to have the maximum element be the root at every recursive call, then recur
#  on the left and right sides of the list
# 
#  In C++ since you can't splice lists, you probably have to pass in left and right indices
def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    def helper(nums):
        if not nums: return None
        root_index = nums.index(max(nums))
        root = TreeNode(nums[root_index])
        root.left = helper(nums[:root_index])
        root.right = helper(nums[root_index + 1:])
        return root
    return helper(nums)