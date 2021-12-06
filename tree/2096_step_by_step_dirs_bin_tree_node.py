# Nathan Zhu, 12/5/2021, 4:44 pm PST, Stockton, CA
# Got a few offers recently inc SF and BBG.  
# Good time to start a new leetcode campaign.
# Leetcode 2096 | medium | fun q
# Category: Binary tree 

# Intuition:
# 
# Ex.      A
#           \
#           B
#            \
#             C
#            / \
#           E   F
#          / \   \
#         G   H   I
#         /       /
#       Start    J
#                  \ 
#                  END
#  Root -> start
#   R R L L L
#  Root -> end 
#   R R R R L R 
#  
#  1. there is a common prefix, we know that this is not part of the path.  We only
#     care about the other stuff
#  2. All moves from start, that are not common prefix are converted to up.
#     We add that to the spliced version of dest not including common prefix for ans

def getDirections(root, startValue, destValue):
    """
    :type root: Optional[TreeNode]
    :type startValue: int
    :type destValue: int
    :rtype: str
    """
    start_path, end_path = [[]], [[]]
    def helper(node, curr_path):
        if not node: return
        
        if node.val == startValue:
            start_path[0] = curr_path[:]
        if node.val == destValue:
            end_path[0] = curr_path[:]
        
        curr_path.append('L')
        helper(node.left, curr_path)
        curr_path.pop()
        curr_path.append('R')
        helper(node.right, curr_path)
        curr_path.pop()
        
    helper(root, [])
    start_path, end_path = start_path[0], end_path[0]
    
    first_diff = 0
    for a, b in zip(start_path, end_path):
        if a != b:
            break
        else: first_diff += 1
    
    return "U" * (len(start_path) - first_diff) + "".join(end_path[first_diff:])
