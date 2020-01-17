# Nathan Zhu 200 Vessey Street, New Yotk, June 26th, 6:00 pm
# Leetcode_230 | medium | idea is easy, implementation may not be as easy, without using recursion.
# 
# Inorder gives you a correct order.  So, you can Get k-smallest in O(h) space with a stack and 
# O(k) time with an iterative inorder traversal.  One big modification that had to be made was
# NOT incrementing when reaching a null node.  Normally, I don't count while doing inorder traversal,
# so considering that was tricky.  

def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    def helper(root, k):
        stack = list()
        curr = root
        
        # I've always had problems with iterative inorder
        # Need to practice this more.
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            # We need this else statement, otherwise we will
            # decrement k everytime we visit a nullptr
            else:
                curr = stack.pop()
                k -= 1
                if k == 0: return curr.val
                curr = curr.right
            
        return -1
    
    return helper(root, k)