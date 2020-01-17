# Nathan Zhu Monday August 12th, 2019.  8:08 pm, Feels kinda strange to not be at work today. New York seems so far away, but so close.
# Leetcode 304 | hard | medium if you see the insight
# 
# This is a pretty hard recursion question, it is kind of subtle, actually.
# I thought so hard about the question, and the solution was so easy...
def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    maximum = [float('-inf')]
    def max_ending_at(root):
        if not root: return 0
        left = max_ending_at(root.left)
        right = max_ending_at(root.right)
        
        # If we take the "biggest" path on left and right, and add it to root.val,
        # we get the biggest path ending at this node. 
        maximum[0] = max(maximum[0], left + root.val + right)
        
        # Returns maximum value single path from this node downwards.
        # The path doesn't need to need to reach a leaf node
        # The path also is 0, if all possible paths are negative.
        return max(root.val + max(left, right), 0)
    
    max_ending_at(root)
    return maximum[0]
        

# This is a TLE approach.
# So, I turn the tree into a fully connected graph, and then go through
# each node to find the biggest path that I can find.
# It is "correct"
def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    def link(root, parent, graph):
        if parent and root:
            graph[parent].append(root)
            graph[root].append(parent)
            
        if root.left: link(root.left, root, graph)
        if root.right: link(root.right, root, graph)
    
    def max_at_n(curr, visited):
        if curr in visited:
            return 0
        visited.add(curr)
        
        total = curr.val
        taken_path = float('-inf')

        # checking parent, left child, right child
        for node in graph[curr]:
            path_down_node = max_at_n(node, visited)
            if path_down_node >= 0:
                taken_path = max(path_down_node, taken_path)
        if taken_path > 0: total += taken_path
        
        # backtrack.
        visited.remove(curr)
        return total
    
    graph = collections.defaultdict(list)
    link(root, None, graph)
    
    returned = float("-inf")
    for key in graph:
        returned = max(returned, max_at_n(key, set()))
        
    return returned
        