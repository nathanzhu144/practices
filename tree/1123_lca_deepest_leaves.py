# Nathan Zhu Amex Tower, 36th floor 7:37 pm, Sunday July 14th, 2019
# Nathan Zhu April 9th, 2020, 12:22 am.  
# Leetcode 1123 | medium | yeet meedium
# Category: B-tree
# Similar questions: finding LCA, smallest subtree with all deepest nodes
#
# Lol, I think this is this exact question.
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# I solved it similarly, and it worked.



def find_lca_deepest_leaves(root):
    def find_height(root):
        if not root: return 0
        node_to_height[root] = max(find_height(root.left), find_height(root.right)) + 1
        return node_to_height[root]
        
    def helper(root):
        if not root: return None
        if not root.left and not root.right: return root    # equal height trees
        if not root.left: return helper(root.right)
        if not root.right: return helper(root.left)
        if node_to_height[root.left] < node_to_height[root.right]: return helper(root.right)
        if node_to_height[root.right] < node_to_height[root.left]: return helper(root.left)
        return root                                          # equal height trees
    
    node_to_height = dict()
    find_height(root)
    return helper(root)
        
# Some other dude's soln, awesome.
# N^2 runtime.
def other_find_lca_deepest(root):
    def helper(root):
        if not root:
            return 0, None
        d1, lca1 = helper(root.left)
        d2, lca2 = helper(root.right)
        if d1 > d2:
            node = lca1
        elif d1 < d2:
            node = lca2
        else:
            node = root
        return max(d1, d2) + 1, node
    return helper(root)[1]

# My new soln, O(N) runtime
def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        table = dict()
        def calc_heights(node):
            if not node: return 0
            table[node] = max(calc_heights(node.left), calc_heights(node.right)) + 1
            return table[node]
            
        
        def get_heights(node):
            if node not in table: return 0
            return table[node]
            
        
        def helper(node):
            if not node: return node
            
            if get_heights(node.left) > get_heights(node.right):
                return helper(node.left)
            elif get_heights(node.left) < get_heights(node.right):
                return helper(node.right)
            else:
                return node
            
        calc_heights(root)
        return helper(root)
