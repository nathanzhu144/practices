# Nathan Zhu Friday Jan 3rd, 2019 6:57 pm
# Leetcode 437 | easy | hard man
# Category: Binary tree
#           This idea is the same idea as one pass two-sum as well as O(N) subarray sum equals k.
import collections

def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    table = collections.defaultdict(int)
    table[0] += 1
    
    ret = [0]
    
    def helper(root, sum_so_far, target):
        if not root: return
        
        find_in_table = root.val + sum_so_far - target
        ret[0] += table[find_in_table]
        table[root.val + sum_so_far] += 1
        
        helper(root.left, sum_so_far + root.val, target)
        helper(root.right, sum_so_far + root.val, target)
        
        table[root.val + sum_so_far] -= 1  # Backtracking here.
    helper(root, 0, sum)
    return ret[0]