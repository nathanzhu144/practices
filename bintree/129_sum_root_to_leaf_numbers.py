#  Nathan Zhu 11:03 am, New York, 55 John Street, 
#  Leetcode 129 | medium | easier-medium
#
#  This has some tricky edge cases, but it standard tree question.
#  
#   Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#   An example is the root-to-leaf path 1->2->3 which represents the number 123.
#   Find the total sum of all root-to-leaf numbers.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Leetcode 129
def sum_numbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def helper(root, curr_path):
        if not root: return 0        # Note: If we hit a nullptr, we need to append 0.  We don't need to append curr_path
                                     #       cause we should've done it earlier.  This handles case of root being an nullptr nicely
        # We append root.val here.
        curr_path.append(str(root.val))

        # If root no right and no left, the path ends here.  Return a number
        if not root.left and not root.right:
            return int("".join(curr_path))

        # Note that if code gets here root.left or root.right.  
        # NOTE: We need curr_path[:] instead of curr_path because we need a shallow copy.  Otherwise,
        #       we will get wack behavior when stuff on the right subtree has numbers from left.
        left = helper(root.left, curr_path[:])
        right = helper(root.right, curr_path[:])
        return left + right
    return helper(root, list())


# Helper function.
def make_tree(vector):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    if not vector: return None
    if len(vector) == 1: return TreeNode(vector[0])
    mid = len(vector) // 2
    
    root = TreeNode(vector[mid])
    root.left = make_tree(vector[:mid])
    root.right = make_tree(vector[mid + 1:])
    return root


if __name__ == "__main__":
    print(sum_numbers(make_tree([1, 2, 3])))