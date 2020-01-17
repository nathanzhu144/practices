# Nathan Zhu 5:09 pm, Monday July 8th, 2019, 36th floor Amex building New York
# Leetcode 95 | medium | medium
# I had trouble with this problem for the longest time, but it makes so much sense as a divide and conq problem.
# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31508/Divide-and-conquer.-F(i)-G(i-1)-*-G(n-i)

def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def helper(start, end):
        # If we cannot make a tree, we return an empty list.
        if start > end: return [None]

        ret = list()
        # we "choose" a root
        for idx in range(start, end + 1):
            # left_trees generates all possible subtrees from indices start .. index - 1, inclusive
            # right trees generates all possible subtrees from indieces index + 1 .. end, inclusive
            left_trees = helper(start, idx - 1)
            right_trees = helper(idx + 1, end)

            for left_t in left_trees:
                for right_t in right_trees:
                    root = TreeNode(idx)
                    root.left = left_t
                    root.right = right_t
                    ret.append(root)

        return ret
    
    if n == 0: return []
    return helper(1, n)