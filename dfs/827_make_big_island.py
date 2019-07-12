# Nathan Zhu, Sunday June 30th, 2019.  10:06 pm We flew over Ann Arbor like 30 min ago.  
# Leetcode 827 | Hard | Solution is long, but not necessarily hard IMO
#
# We do a DFS on each island in grid, and mark each with a different color.  
#
# Then we iterate through the matrix again, and see which spot we can fill in to connect
# the most landmass.
#
# https://leetcode.com/problems/making-a-large-island/discuss/127015/C%2B%2B-O(n*m)-15-ms-colorful-islands
def make_large_island(matrix):
    def largestIsland(self, matrix):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def in_bounds(matrix, row, col):
        return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])
    
    # Paints an island, and returns how big that color island is
    def color_island(matrix, row, col, color):
        if not in_bounds(matrix, row, col) or matrix[row][col] != 1: return 0
        ret = 0
        
        matrix[row][col] = color
        ret += color_island(matrix, row + 1, col, color)
        ret += color_island(matrix, row - 1, col, color)
        ret += color_island(matrix, row, col + 1, color)
        ret += color_island(matrix, row, col - 1, color)
        return 1 + ret
    
    # If we create a new island here, how big will it be?
    def new_island_size(matrix, row, col, color_to_island_size):
        conn_colors = set()
        
        conn_colors.add(matrix[row][col])     # we could be standing on a square of size 1 right now
        # we try to see what new colors we can get by looking at surrounding 4 squares
        if in_bounds(matrix, row + 1, col): conn_colors.add(matrix[row + 1][col])
        if in_bounds(matrix, row - 1, col): conn_colors.add(matrix[row - 1][col])
        if in_bounds(matrix, row, col + 1): conn_colors.add(matrix[row][col + 1])
        if in_bounds(matrix, row, col - 1): conn_colors.add(matrix[row][col - 1])
            
        # If matrix[row][col] is a 0, we add 1 when we add a piece of land there.  Otherwise, it is already connected there,
        # we shouldn't add one in that case.  Also note that 0 is not a color, so if we see a 0 ignore it.
        return sum([color_to_island_size[color] for color in conn_colors if color != 0]) if matrix[row][col] != 0 else \
            sum([color_to_island_size[color] for color in conn_colors if color != 0]) + 1
            

    # Data structures #
    # Hash table for color -> size of island (color_to_island_size)
    color_to_island_size = dict()
    color = 2
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            color_to_island_size[color] = color_island(matrix, row, col, color)
            color += 1

    ret_max_isla = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ret_max_isla = max(ret_max_isla, new_island_size(matrix, row, col, color_to_island_size))

    return ret_max_isla