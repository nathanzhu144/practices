# Nathan Zhu Amex Building 36th floor, Sunday July 14th, 2019, 12:04 pm
# Leetcode 589 | easy | EZ
# 
# So, there's a harder way to preorder/postorder iteratively, and there's a super simple way.
# This is the super simple way.
#

def nary_preorder(root):
    if not root: return []
    stack, ret = [root], []

    while stack:
        curr = stack.pop()
        ret.append(curr.val)

        # We push onto stack rightmost child to leftmost child
        # this guarnatees we visit leftmost child first
        for child in curr.children[::-1]:
            stack.append(child)
    return ret
