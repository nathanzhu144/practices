#  Nathan Zhu, New York, Amex tower, 8:32 am
#  Leetcode medium.
# This question was the easiest medium I've ever done, literally took < 1 min to finish
#
# If you look at a binary tree from the right what do you see?
# Do a level order traversal...

def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root: return list()
    BFS_curr, BFS_next = [root], list()
    side_view = list()
    
    while BFS_curr:
        side_view.append(BFS_curr[-1].val)    # append last element of each "level" of tree
        while BFS_curr:
            front = BFS_curr.pop(0)
            if front.left: BFS_next.append(front.left)
            if front.right: BFS_next.append(front.right)
        BFS_curr = BFS_next[:]
        BFS_next = list()
    return side_view