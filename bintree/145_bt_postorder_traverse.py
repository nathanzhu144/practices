# Nathan Zhu 3:39 pm.  American Express Building, 200 Vessey Street, Friday July 12th, 2019
# Leetcode 145 | hard | hard as hell if you don't know trick; otherwise easy
#
# 

# So, here's a cool trick.  Doing an iterative pre-order is extremely easy.
# If you do a modified pre-order traversal, where you explore the right before the left
# and you reverse it, you did a postorder traversal.
def postorder_iterative(root):
    if not root: return None
        ret = []
        stack = [root]

        while stack:
            curr = stack.pop()
            ret.append(curr.val)

            # Note how we push left onto stack before we push right onto the stack.
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)

    # we return reversed sequence.
    return ret[::-1]