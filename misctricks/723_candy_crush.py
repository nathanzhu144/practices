# Nathan Zhu January 22nd, 2019 12:50 pm North Quad justed if .idx in python is implemented with a rabin karp rolling hash. Didn't know the answer
# Leetcode 723 | medium | medium
# Category: Fizzbuzz 

def candyCrush(self, board):
    """
    :type board: List[List[int]]
    :rtype: List[List[int]]
    """
    
    if not board or not board[0]: return board
    
    R, C = len(board), len(board[0])
    while True:
        # Find all things to mark as 0.
        removed = set()
        for r in range(R):
            for c in range(C):
                if r >= 2 and board[r][c] != 0 and board[r][c] == board[r - 1][c] and board[r][c] == board[r - 2][c]:
                    removed |= {(r, c), (r - 1, c), (r - 2, c)}
                if c >= 2 and board[r][c] != 0 and board[r][c] == board[r][c - 1] and board[r][c] == board[r][c - 2]:
                    removed |= {(r, c), (r, c - 1), (r, c- 2)}
        
        # IF nothing to remove, we are done
        if len(removed) == 0: break
        # Crush
        for r, c in removed: board[r][c] = 0
        
        # Drop
        # I think the harder part is this part:
        # The idea behind this is simple: 
        # For each column: 
        #
        #  [7]           [0]
        #  [0]    ->     [0]
        #  [0]           [7] 
        #  [2]           [2]
        #  [1]           [1]
        # To do this, simply go from bottom to top with a read idx and a write idx.
        # 
        for c in range(C):
            ridx = R - 1
            for r in reversed(range(R)):
                if board[r][c] != 0: 
                    board[ridx][c] = board[r][c]
                    ridx -= 1
            for r in range(ridx + 1):
                board[r][c] = 0
    return board

if __name__ == "__main__":
    print(candyCrush([1, 1, 1, 0, 1, 0],
                     [0, 0, 1, 1, 1, 0]]))
