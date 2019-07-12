#  Nathan Zhu Tuesday July 9th, 2019, 9:26 am
#  Leetcode 1034 | medium | about medium-ish, like a harder medium.
#  
#  This is a great visual explanation.
#  https://leetcode.com/problems/coloring-a-border/discuss/282847/C%2B%2B-with-picture-DFS
#
#  Hardest part of this problem for me was a RAW hazard (read after write).  
#  When you are checking to see whether a square is a border square, you could have overwritten
#  the surrounding squares already, making the results kinda strange.  

def color_border(grid, row, col, color):
    """
    :type grid: List[List[int]]
    :type r0: int
    :type c0: int
    :type color: int
    :rtype: List[List[int]]
    """
    positions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    def is_invalid(grid, row, col):
        return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])
    
    # Color this island to the negative of its old color.  So, if island is of 2s, they become -2s.
    def color_negative(grid, row, col, oldcolor):
        if is_invalid(grid, row, col) or grid[row][col] != oldcolor: return
        grid[row][col] = -oldcolor  # color to negative of old color here
        
        for pos in positions:
            new_row, new_col = row + pos[0], col + pos[1]
            color_negative(grid, new_row, new_col, oldcolor)
    
    # We re-visit all negative squares
    def get_border_squares(grid, row, col, oldcolor):
        # This square is off board, is not negative of old color or has been visited already.
        if is_invalid(grid, row, col) or grid[row][col] != -oldcolor or \
                  [row, col] in oldcolor_coords or [row, col] in newcolor_coords: return
        
        # We check here if it is a border square, i.e. is any adj square not negative of oldcolor is is out of bounds
        is_border = False
        for pos in positions:
            new_row, new_col = row + pos[0], col + pos[1]
            if is_invalid(grid, new_row, new_col) or not grid[new_row][new_col] == -oldcolor:
                is_border = True
        
        if is_border: newcolor_coords.append([row, col])     # is border square
        else: oldcolor_coords.append([row, col])             # is non-border square
        
        for pos in positions:
            new_row, new_col = row + pos[0], col + pos[1]
            get_border_squares(grid, new_row, new_col, oldcolor)

    oldcolor_coords = list()
    newcolor_coords = list()
    oldcolor = grid[row][col]
    color_negative(grid, row, col, oldcolor)
    get_border_squares(grid, row, col, oldcolor)
    for sq in oldcolor_coords: grid[sq[0]][sq[1]] = oldcolor     # re-colors all non-border coords to old non-negative color
    for sq in newcolor_coords: grid[sq[0]][sq[1]] = color        # colors all border coordinates here to "color"
    return grid

if __name__ == "__main__":
    print(color_border([[1,2,1,2,1,2],
                        [ 2,2,2,2,1,2],
                        [ 1,2,2,2,1,2]],
                        1,
                        3,
                        1))
            

# [[1,2,1,2,1,2],
# [ 2,2,2,2,1,2],
# [ 1,2,2,2,1,2]]
# 1
# 3
# 1
# Output:
# [[1,1,1,1,1,2],
# [ 1,1,1,1,1,2],
#  [1,1,1,1,1,2]]
# Expected:
# [[1,1,1,1,1,2],
#  [1,2,1,1,1,2],
#  [1,1,1,1,1,2]]