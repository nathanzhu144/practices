# Nathan Zhu Saturday 9:36 pm January 3rd, 2019 Amber just came to play board games, Dom came earlier too.
# Leetcode 113 | medium | EZ
# Category: Btree
# Basic backtracking.

def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    
    ret = []
    def helper(root, curr_seq, curr_sum, target):
        if not root: return
        
        curr_seq += [root.val]
        curr_sum += root.val
        
        if not root.left and not root.right:
            if curr_sum == target:
                ret.append(curr_seq[:])
                
        helper(root.left, curr_seq, curr_sum, target)
        helper(root.right, curr_seq, curr_sum, target)
            
        curr_seq.pop()
        curr_sum -= root.val
        
    helper(root, [], 0, sum)
    return ret