 # Nathan Zhu, Thursday 4:05 pm August 22nd, 2019
 # Leetcode 427 | medium | medium
 # Category: Data structure
 # 
 # Never seen or heard of a quad tree until today, but quad trees are used to represent a lot of things.
 #
 # What does a quad tree do?
 # 
 # In this case, we use to represent a 0-1 matrix, where we stop recursing down when we get a 0 or 1 for
 # everything in that subquadrant.
 #
 # We can also use it for image compression, where each recursive level of the quadtree results in a 
 # certain level of image quality.
 #
 # A region quadtree may also be used as a variable resolution representation of a data field. 
 # For example, the temperatures in an area may be stored as a quadtree, with each leaf node
 # storing the average temperature over the subregion it represents.
 # 
 # Spatial indexing (like geohashing) can be easily represented with a quad tree. 
 
 def construct(grid):
    """
    :type grid: List[List[int]]
    :rtype: Node
    """
    # Observations.  If all grid elements are same, we stop recursing.
    #                Otherwise, we recurse further...
    def helper(grid):
        value = grid[0][0]
        is_leaf = True
        
        # check if it is all true or all false
        is_leaf = all(grid[row][col] == grid[0][0] for row in range(len(grid)) for col in range(len(grid[0])))
        
        # if it is a leaf, we are done recursing down.
        if is_leaf: return Node(value, True, None, None, None, None)
        
        size = len(grid)
        return Node('*',
                    False, 
                    helper([row[:size // 2] for row in grid[:size // 2]]),     # NW
                    helper([row[size // 2:] for row in grid[:size // 2]]),     # NE
                    helper([row[:size // 2] for row in grid[size // 2:]]),     # SW
                    helper([row[size // 2:] for row in grid[size // 2:]]))     # SE
    return helper(grid)