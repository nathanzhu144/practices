# Nathan Zhu Amex Building 36th floor, Sunday July 14th, 2019, 12:23 pm
# Leetcode 590 | easy | EZ
# 
# So, there's a harder way to preorder/postorder iteratively, and there's a super simple way.
# This is the super simple way.
#

def nary_postorder(root):
    if not root: return []
    stack, ret = [root], []

    while stack:
        curr = stack.pop()
        ret.append(curr.val)

        for child in curr.children:
            stack.append(child)
    return ret[::-1]