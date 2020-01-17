# Nathan Zhu Amex Tower 2:13 pm, New York, NY
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/s
#
# The idea is convert linked list to a vector.  Then, recursively construct a 
# height balanced tree from the vector, which is pretty trivial.  You make the 
# center element the root, and recur on left and right sections of the vector.
#
# There are cooler solns that use O(1) space, but this beats 98% in time.

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    inorder_vec = list()
    while head:
        inorder_vec.append(head.val)
        head = head.next
        
    def helper(inorder_vec):
        if not inorder_vec: return None
        root_index = len(inorder_vec) / 2
        root = TreeNode(inorder_vec[root_index])
        root.left = helper(inorder_vec[:root_index])
        root.right = helper(inorder_vec[root_index + 1:])
        return root
    
    return helper(inorder_vec)