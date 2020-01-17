#  Nathan Zhu, American Express Building 36th floor 10:56 am
#  Leetcode 109 | Easy | really fucking easy
#   
#  Given a binary tree, return the bottom-up level order traversal
#  of its nodes' values. (ie, from left to right, level by level from leaf to root).
#  
#  Should know this by heart.


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    ret = [[root.val]]
    BFS = [root]
    
    while BFS:
        BFS_next = list()
        for node in BFS:
            if node.left: BFS_next.append(node.left)
            if node.right: BFS_next.append(node.right)
        if BFS_next: ret.append([node.val for node in BFS_next])
        BFS = BFS_next[:] 
    
    return ret[::-1]