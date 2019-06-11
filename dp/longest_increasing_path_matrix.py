def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    
    # returns true if selected matrix is an OK move, as in
    #  1. It is in bounds
    #  2. It has a greater val than curr square
    def is_valid_move(matrix, row_in, col_in, curr_square_val):
        if row_in < len(matrix) and col_in < len(matrix[0]) \
                                and row_in >= 0 and col_in >= 0 \
                                and matrix[row_in][col_in] > curr_square_val:
            return True
        else:
            return False
        
    def DFS(matrix, row, col, visited):
        move = (row, col)
        
        if move in visited:
            return visited[move]
        
        #base case, if we cannot make any moves, the longest increasing path is 1
        if not is_valid_move(matrix, row + 1, col, matrix[row][col]) and not is_valid_move(matrix, row - 1, col, matrix[row][col]) \
            and not is_valid_move(matrix, row, col + 1, matrix[row][col]) and not is_valid_move(matrix, row, col - 1, matrix[row][col]):
            visited[move] = 1
            return visited[move]
        #there exists a valid move, so we want to find the max move we can get
        else: 
            max_path = max[DFS(matrix, row + 1, col, visited), DFS(matrix, row - 1, col, visited), DFS(matrix, row , col + 1, visited), DFS(matrix, row , col - 1, visited)] + 1
            visited[move] = max_path
            return visited[move]
                            
                            
            
        
    def find_longest_increasing_path(matrix):
        
        visited = dict()  #visited should map   (row, col) -> longest increasing path from (row, col)
        longest_path = 0
                            
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                move = (row, col)
                longest_path = max(longest_path, DFS(matrix, row, col, visited))
                
        return longest_path
                        
    return find_longest_increasing_path(matrix)
                        

if __name__ == "__main__":
    print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))