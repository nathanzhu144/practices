# /* Nathan Zhu Monday July 14th, 2020  Stockton, CA. Went to Nelson Park today.
# *  Deploying golang projects to Heroku is really fun.  :P
# *  Leetcode 1506 | medium | medium 
# *  Category: tree
# */

def findRoot(tree):
    """
    :type tree: List['Node']
    :rtype: 'Node'
    """
    # A space-taking soln will use the fact that in-degree of root is 0, which
    # is not true for any other node
    #
    # Space-eff soln uses the fact all nodes have unique values.
    # All non-root vals are "seen" twice, once from perspective of its parent, and
    # again from its perspective as a parent 
    #
    # We could use XOR, or addition to find the only node which is not seen from the
    # perspective of a parent. 
    # 
    ret = 0
    for node in tree:
        ret ^= node.val
        for child in node.children: ret ^= child.val
            
    # all vals unique, so when we see node with val we want to find, return this node
    for node in tree:
        if node.val == ret: return node
    return None # should never get here