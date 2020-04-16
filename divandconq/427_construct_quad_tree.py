 # Nathan Zhu, Thursday 4:05 pm August 22nd, 2019
 #             March 23rd, 2020 1:59 am Stockton, CA
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


def construct_worse(self, grid):
 	"""
	:type grid: List[List[int]]
	:rtype: Node
	"""
	def helper(grid, sr, sc, er, ec):
	    if not grid: return None
	    
	    val = grid[sr][sc]
	    all_same = True
	    for r in range(sr, er + 1):
		for c in range(sc, ec + 1):
		    if grid[r][c] != val:
			all_same = False
		if not all_same: break
		    
	    if all_same: return Node(val, True, None, None, None, None)
	    
	    rowsize, colsize = er - sr + 1, ec - sc + 1
	    midrowm1, midrow = sr + rowsize // 2 - 1, sr + rowsize // 2
	    midcolm1, midcol = sc + colsize // 2 - 1, sc + colsize // 2
	    tl = helper(grid, sr, sc, midrowm1, midcolm1)
	    tr = helper(grid, sr, midcol, midrowm1, ec)
	    bl = helper(grid, midrow, sc, er, midcolm1)
	    br = helper(grid, midrow, midcol, er, ec)
	    return Node(-1, False, tl, tr, bl, br)
	return helper(grid, 0, 0, len(grid) - 1, len(grid[0]) - 1)
	    
            
