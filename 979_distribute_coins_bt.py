# Nathan Zhu September 4, 2019 10:58 PM
# Leetcode 979 | medium | kinda challenging actually
# Microsoft- Phone Interview on leetcode
# Time Spent: 1 hour 20 minutes 31 seconds
# Time Allotted: 1 hour 30 minutes

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/256224/Python-DFS-with-(quite)-detailed-explanation
def distributeCoins(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    ret = [0]
    def helper(root):
        if not root: return 0
        
        # Left is how much left tree needs to be balanced
        # Right is how much right tree needs to be balanced
        left = helper(root.left)
        right = helper(root.right)
        
        # We increment ret by number of coins we need to move to left and right subchild
        ret[0] += (abs(left) + abs(right))
        
        # root.val - 1 is to account for the fact that this node needs a coin
        return left + right + root.val - 1
    
    helper(root)
    return ret[0]