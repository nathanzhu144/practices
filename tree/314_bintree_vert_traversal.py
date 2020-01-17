# Nathan Zhu, Sunday August 4th, 4:03 am.  EHS 55 John Street.  My roommate just had sex very loudly and I couldn't
#                                          fall asleep, 
# Leetcode 314 | medium | medium
# Category: Binary tree / Hashtable
# 
# Let's first talk about the intuition. 
# table maps   vertical level -> list of nodes on that level
#
# Ex.
#    
# Vertical levels:
#   
#    -2  -1  0  1  2
#            4
#          /    \
#         2      6
#      /   \  /   \
#    -1     3 5    8
#  
#  table = { -2 : [-1],
#            -1 : [2],
#             0 : [4, 3, 5] ...}
#
# So, this question is easy if we don't care about the ordering, but
# we need to  follow two rules:
# 
# 1. We need to print from top to bottom in each vertical row
# 2. We need to print from left to right if there's a tie.
# 
# My recursive function goes from left to right, in a pre-order traversal
# so, we know the left to right ordering is maintained.
# However, to solve the vertical problem, I also push in the depth and 
# end up sorting each list by depth.  Since python sort is stable, this
# maintains left-right tie break.

def verticalOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    
    def helper(root, horizontal, depth):
        if not root: return
        
        table[horizontal].append([root.val, depth])
        leftmost[0] = min(horizontal, leftmost[0])
        rightmost[0] = max(horizontal, rightmost[0])
        
        helper(root.left, horizontal - 1, depth + 1)
        helper(root.right, horizontal + 1, depth + 1)
        
    if not root: return []
    leftmost = [0]
    rightmost = [0]
    table = collections.defaultdict(list) # maps vert -> list of nodes
                                            # we always go left to right
    helper(root, 0, 0)
    ret = []
    for i in range(leftmost[0], rightmost[0] + 1):
        temp = []
        for node in sorted(table[i], key = lambda x: x[1]):
            temp.append(node[0])
        ret.append(temp)
    
    return ret
                