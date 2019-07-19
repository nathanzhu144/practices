#  Nathan Zhu June 26th, 2019
#  Leetcode 329 | hard | yeah hard
#
#  June 20th, 2019 
#  3:56 pm, New York, NY  Longest increasing path matrix
#  This is a classic DP problem.  
#
#  Suppose that we have found the longest increasing path at row, col.  Then, when we are
#  calculating from another square, we hit that square again.  The longest path is simply 
#  that length plus current length.

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    
    # Returns true if a move is in bounds
    def is_in_bounds(matrix, row_in, col_in):
        return row_in < len(matrix) and col_in < len(matrix[0]) and row_in >= 0 and col_in >= 0

    # Returns true if a square is in bounds and new square is bigger than old square
    def is_valid_move(matrix, row_in, col_in, curr_square_val):
        return is_in_bounds(matrix, row_in, col_in) and matrix[row_in][col_in] > curr_square_val

    
    # Visited is whether a row, col has been called by the function DFS
    # mem stores the result of the function DFS
    #
    # In the case where DFS calls itself, it is possible that we revisit the same square before we 
    # have finished calculating the result of that square, so ...
    # if move in visited and move not in mem: return 0
    def DFS(matrix, row, col, visited, mem):
        if not is_in_bounds(matrix, row, col): return 0

        move = (row, col)
        if move in visited and move not in mem: return 0
        visited.add(move)
        if move in mem: return mem[move]
        
        #base case, if we cannot make any moves, the longest increasing path is 1
        if not is_valid_move(matrix, row + 1, col, matrix[row][col]) and not is_valid_move(matrix, row - 1, col, matrix[row][col]) \
            and not is_valid_move(matrix, row, col + 1, matrix[row][col]) and not is_valid_move(matrix, row, col - 1, matrix[row][col]):
            mem[move] = 1

        #there exists a valid move, so we want to find the max move we can get
        else: 
            max_path = 0
            if is_valid_move(matrix, row + 1, col, matrix[row][col]): max_path = max(DFS(matrix, row + 1, col, visited, mem), max_path)
            if is_valid_move(matrix, row - 1, col, matrix[row][col]): max_path = max(DFS(matrix, row - 1, col, visited, mem), max_path)
            if is_valid_move(matrix, row, col + 1, matrix[row][col]): max_path = max(DFS(matrix, row, col + 1, visited, mem), max_path)
            if is_valid_move(matrix, row, col - 1, matrix[row][col]): max_path = max(DFS(matrix, row, col - 1, visited, mem), max_path)

            mem[move] = max_path + 1
        return mem[move]
        
    def find_longest_increasing_path(matrix):
        if not matrix: return 0
        visited = set()  #visited should map   (row, col) -> longest increasing path starting from (row, col)
        mem = dict()
        longest_path = 0
                        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                longest_path = max(longest_path, DFS(matrix, row, col, visited, mem))   
        return longest_path
                        
    return find_longest_increasing_path(matrix)

if __name__ == "__main__":
    print(longestIncreasingPath([[7,8,9],
                                 [9,7,6],
                                 [7,2,3]]))