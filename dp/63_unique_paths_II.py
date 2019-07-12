#  NAthan Zhu, Amex Tower, 36th floor, 10:26 pm, 200 Vessey Street
#  Leetcode 63 | medium | easy-medium
#
#  This is a twist on unique_paths_II.  The idea is actually very idea.
#  If a square is blocked, return 0.
# 
def unique_paths_II(matrix):   
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    def helper(matrix, row, col, mem):
        key = (row, col)
        if key in mem: return mem[key]

        ret = 0
        # DO NOT MAKE mem[key] here. It DOES contiminate other solutions.  Make the hash table entry at bottom.

        # If there is a 1 at this square, no paths, return 0 (note, this takes priority over row == 0 and col == 0)
        if matrix[row][col] == 1: return 0
        elif row == 0 and col == 0: return 1                       # If we reached bottom square, return 1
        elif col == 0: ret = helper(matrix, row - 1, col, mem)     # we got to left of board
        elif row == 0: ret = helper(matrix, row, col - 1, mem)     # we got to top of board
        else: ret = helper(matrix, row - 1, col, mem) + helper(matrix, row, col - 1, mem)   

        mem[key] = ret
        return ret
    
    return helper(matrix, len(matrix) - 1, len(matrix[0]) - 1, dict())

if __name__ == "__main__":
    print(unique_paths_II([[0,0,0],
                            [0,1,0],
                            [0,0,0]]))
