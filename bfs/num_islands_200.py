#  Count the number of islands
#  Leetcode 200 | medium | I think easy
#  Nathan Zhu 12:40 pm at Amex Tower New York, June 13th, 2019
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def sink(grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return
        
        grid[row][col] = "0"
        sink(grid, row + 1, col)
        sink(grid, row - 1, col)
        sink(grid, row, col + 1)
        sink(grid, row, col - 1)
    
    counter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                counter += 1
                sink(grid, row, col)
                
    return counter