# Nathan Zhu Stockton, CA, COVID-19.  Salesforce internship starting in 2 weeks, got an A+ in 376, aced that binary search question
#                              in 376 final.  What a blast!
# Leetcode 637 | easy | easy
# Category: btree


def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    q = [root]
    ret = []
    
    while q:
        newq = []
        tot = 0
        for node in q:
            tot += node.val
            if node.left: newq.append(node.left)
            if node.right: newq.append(node.right)
        ret.append(tot * 1.0 / len(q))
        q = newq
        
    return ret