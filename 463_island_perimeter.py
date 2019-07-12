# Nathan Zhu Tuesday 9:51 am.  Amex tower, 36th floor.
# Leetcode 463 | easy | easy
#
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
# and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.
# 
# We know that there is exactly one island.
def find_perimeter(grid):

     def is_invalid(grid, row, col):
            return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])
        def count_perimeter(grid, row, col):
            if is_invalid(grid, row, col) or grid[row][col] != 1 or (row, col) in visited: return 0
            visited.add((row, col))

            # counter perimeter of this square
            perimeter = 0
            for pos in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_row, new_col = row + pos[0], col + pos[1]
                if is_invalid(grid, new_row, new_col) or grid[new_row][new_col] == 0: perimeter += 1
            # recur for surrounding islands
            for pos in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_row, new_col = row + pos[0], col + pos[1]
                perimeter += count_perimeter(grid, new_row, new_col)

            return perimeter


        visited = set()
        row_start, col_start = -1, -1
        # find a square of island
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1: row_start, col_start = row, col

        return count_perimeter(grid, row_start, col_start)
    