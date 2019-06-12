#  Nathan Zhu Amex Building 36th Floor, 12:00 pm lunch break, 200 Vessey Street, New York, NY
#
#  How to figure out whether a word exists in a board?
#
#  Ex. Does "WORD" exist in this board?  XXXXW    Yes.
#                                        XXDRO 
#                                               
#  This is a classic BFS problem that took me too long.  There are some tricky edge cases.
#  I figured out pretty quickly that if was important to iterate through whole board and do
#  a DFS at each square.
#
#  One problem I didn't anticipate was marking squares as visited.
#
#  Ex. XXXX
#      XABC
#
#  Suppose that we are trying to find the string "ABCBA".  If we just do a pure DFS
#  without keeping track of visited squares, we will be able to find "ABCBA" in the board
#  by simply going A -> B -> C -> B (revisited) -> A (revisited)
#
#  Then, when I added in marking squares as visited, I was pruning too many possibilities.
#  
#  The solution is to mark a square as visited, and when you return from the recursive call,
#  un-marking the square as visited.
#  
def exist(board, word):
    # Returns true if a square is in bounds of board and it has the desired character
    def is_valid_move(board, row, col, target):
        if row < len(board) and col < len(board[0]) and row >= 0 and col >= 0 and board[row][col] == target:
            return True
        else:
            return False

    # Check whether a word starting at this point can work.
    # Note the order of 1, 2, and 3 are extremely important. If we check whether we have found
    # the whole string (#2) before checking if the spot has been visited, we can return true in a case like
    #  [["A", "A"], "AAA"]
    # 
    # If we check whether a move is valid (#3) before we check (#2), we can get an out of bounds,
    # as an empty string has no first
    def DFS(board, curr_row, curr_col, string, visited):
        spot = (curr_row, curr_col)
        
        # 1. making sure we don't visit the same spot twice
        if spot in visited:
            return False
        
        # 2. We have found the whole string
        if not string:
            return True
        
        # 3. this move is not valid
        if not is_valid_move(board, curr_row, curr_col, string[0]):
            return False
        
        # we have visited this spot, don't revisit it
        visited.add(spot)

        returned = DFS(board, curr_row + 1, curr_col, string[1:], visited) or DFS(board, curr_row - 1, curr_col, string[1:], visited) or \
                    DFS(board, curr_row, curr_col + 1, string[1:], visited) or DFS(board, curr_row, curr_col - 1, string[1:], visited)
        
        # we have backtracked, and are not using this spot anymore
        visited.remove(spot)
        return returned
    
    # Iterating thru whole board.
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if DFS(board, row, col, word[:], set()):
                    return True

    return False
if __name__ == "__main__":
    print(exist([["A","A"]], "AAA"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))