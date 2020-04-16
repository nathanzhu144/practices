# Nathan Zhu Jan 5th, 2020.  12:29 pm SI 106, we have exam tomorrow, lol.
# Leetcode 270 | easy | easy
# Category: binary tree


def closest_val(root, target):
    def helper(root, target):
        if not root: return float('inf'), None
        if root.val == target: return (0, root.val)
        
        diff, val = abs(root.val - target), root.val
        
        if root.val > target: 
            ldiff, lval = helper(root.left, target)
            return (ldiff, lval) if ldiff < diff else (diff, val)
        if root.val < target: 
            rdiff, rval = helper(root.right, target)
            return (rdiff, rval) if rdiff < diff else (diff, val)
        
    return helper(root, target)[1]