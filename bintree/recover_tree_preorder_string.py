
#  Nathan Zhu, 11:34 pm, Amex Building, New York, NY
#  
#  https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/discuss/274621/JavaC%2B%2BPython-Iterative-Stack-Solution
# 
# We save the construction path in a stack.
# In each loop,
# we get the number level of '-'
# we get the value val of node to add.

# If the size of stack is bigger than the level of node,
# we pop the stack until it's not.

# Finally we return the first element in the stack, as it's root of our tree.
    
    
def recoverFromPreorder(S):
    """
    :type S: str
    :rtype: TreeNode
    """
    stack = list()
    i = 0
    
    while i < len(S):
        level = 0
        val = str()
        # We figure out how many levels down the node is
        while i < len(S) and S[i] == "-":
            level, i = level + 1, i + 1
        # We figure out how big the number is, like "234" has multiple chars
        while i < len(S) and S[i] != "-":
            val, i = val + S[i], i + 1
        node = TreeNode(val)

        # We are done with all nodes currently above level, so we pop them
        while level < len(stack):
            stack.pop(-1)

        # Now: level == len(stack)
        #      If it does not have a left, we attach to left.
        #      If it does have a left, but not a right, we attach to right.
        # NOTE: we need if stack because for the very first iteration
        #       of while loop, there is no stack
        if stack and not stack[-1].left:
            stack[-1].left = node
        elif stack:
            stack[-1].right = node

        # We push current node onto stack, so can append children on it in future
        stack.append(node)
    return stack[0]