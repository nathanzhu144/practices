# Nathan Zhu, Amex, 200 Vessey Street, 36th floor, Friday July 12th, 2019
# Leetcode 110 | easy | yeah really easy
# Category: tree
#
# Naive solution is O(N^2) cause you re-caculate height for each node.
# This solution uses a hash table to map all nodes to their heights, making it O(n) time and O(n) space.

def is_height_balanced(root):
    def map_node_to_height(root, node_to_height):
        if not root: return 0
        node_to_height[root] = max(map_node_to_height(root.left, node_to_height), map_node_to_height(root.right, node_to_height)) + 1
        return node_to_height[root]

    def helper(root, node_to_height):
        if not root: return True
        l_height, r_height = 0, 0
        if root.left: l_height = node_to_height[root.left]
        if root.right: r_height = node_to_height[root.right]
        return abs(l_height - r_height) < 2 and helper(root.left, node_to_height) and helper(root.right, node_to_height)

    node_to_height = dict()
    map_node_to_height(root, node_to_height)
    return helper(root, node_to_height)