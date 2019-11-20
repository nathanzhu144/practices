# Nathan Zhu Thuesday Sepetember 10th, 2019
# Leetcode 773 | hard | hard
# Category: BFS

# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
#  and an empty square represented by 0.

# A move consists of choosing 0 and a 4-directionally adjacent number and
#  swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].


def slidingPuzzle(board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    
    # Returns true if a board is solved.
    # Returns false otherwise
    def solved(board_in):
        for l, r in zip(board_in, [1, 2, 3, 4, 5, 0]):
            if l != r: return False
        return True
    
    # Initializing the move set from 2d to 1d
    raw_moves = [(0, [1, 3]), (1, [0, 2, 4]), (2, [1, 5]), (3, [0, 4]), (4, [1, 3, 5]), (5, [2, 4])]
    moves = dict()
    for start, end in raw_moves:
        moves[start] = end
        
    # Copying the board from a 2d board to a 1d modified board
    mod_board = list()
    start = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            mod_board.append(board[row][col])
            if board[row][col] == 0: start = len(board[0]) * row + col
    
    
    # Q: (represents a queue, but is a list of pairs of a (current board, position, where zero is on board)
    # visited: a set of boards in form (1, 3, 4, 0, 2, 5) for example
    Q = [(mod_board, start)]
    visited = set([tuple(mod_board)])
    ret = 0
    if solved(mod_board): return ret
    
    # typical BFS
    while Q:
        ret += 1
        next_Q = list()
        
        for curr_board, zero_pos in Q:
            for neighbor in moves[zero_pos]:
                newboard = curr_board[:]
                newboard[neighbor], newboard[zero_pos] = newboard[zero_pos], newboard[neighbor]
                if tuple(newboard) in visited: continue
                visited.add(tuple(newboard))
                if solved(newboard): return ret
                
                next_Q.append((newboard, neighbor))
                
        Q = next_Q
    # we have run out of moves to make
    return -1