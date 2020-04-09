# Nathan Zhu March 23rd, 2020. Foundry Lofts during COVID-19
# Leetcode 103 | medium | EZ
# Category: Binary tree


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    q = [root]
    ret = []
    idx = 0
    
    while q:
        newq = []
        curr = []
        for node in q:
            if node.left: newq.append(node.left)
            if node.right: newq.append(node.right)
            curr.append(node.val)
            
        if idx & 1: ret.append(curr[::-1][:])
        else: ret.append(curr[:])
        
        q = newq
        idx += 1
    return ret