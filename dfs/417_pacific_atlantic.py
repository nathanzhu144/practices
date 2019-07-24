#  Nathan Zhu July 2nd, 2019 6:47 pm
#  Leetcode 417 | medium | I think harder medium
#  
#  My original idea was to do a DFS from each row, col to see whether it can get to atlantic ocean
#  and pacific ocean.  
# 
#  It is a much better idea to see which squares each ocean can get to, by doing a DFS from each ocean
#  and iterate thru matrix checking to see whether that square has been visited by oceans.
#  

#  args: matrix   ->  ret: list[]
def pacific_atlantic(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    def is_valid(matrix, row, col):
        return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])
    
    # attempt to mark all squares that can get to that ocean
    # We use this later to do a DFS from each ocean square and see which squares we can cover.
    def dfs(matrix, row, col, ocean_mem):
        key = (row, col)
        ocean_mem[key] = True

        # we check each move to see if it is on the board and the height is higher (since we are going from ocean)
        # note that we check that (new_row, new_col) is not in ocean_mem... this stops infinite recursion.
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if is_valid(matrix, new_row, new_col) and (new_row, new_col) not in ocean_mem and matrix[new_row][new_col] >= matrix[row][col]: 
                dfs(matrix, new_row, new_col, ocean_mem)
                

    if not matrix: return []
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    atlantic_mem, pacific_mem = dict(), dict()         # Maps coordinates (row. col) to whether they can get to that ocean
    ret = list()

    # p_visited[i][0] = True
    # a_visited[i][n-1] = True
    for row in range(len(matrix)):
        dfs(matrix, row, 0, pacific_mem)
        dfs(matrix, row, len(matrix[0]) - 1, atlantic_mem)

    # p_visited[0][j] = True
    # a_visited[m-1][j] = True
    for col in range(len(matrix[0])):
        dfs(matrix, 0, col, pacific_mem)
        dfs(matrix, len(matrix) - 1, col, atlantic_mem)
        
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row, col) in pacific_mem and (row, col) in atlantic_mem:
                ret.append([row, col])
    return ret

if __name__ == "__main__":
    print(pacific_atlantic([[1,2,2,3,5],
                           [3,2,3,4,4],
                           [2,4,5,3,1],
                           [6,7,1,4,5],
                           [5,1,1,2,4]]))