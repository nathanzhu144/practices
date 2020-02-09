# Nathan Zhu Feb 1st, 2020.  Foundry Lofts, Michale turned temp to 67 today.
# Leetcode 419 | medium | dang didn't think of this
# Category: misc tricks
# We want to find the number of battleships in 1 pass and without extra space and without modifying board.
# 

def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    if not board or not board[0]: return 0
    
    ret = 0
    R, C = len(board), len(board[0])
    
    for r in range(R):
        for c in range(C):
            if board[r][c] == "X" and (r == 0 or board[r - 1][c] == ".") and (c == 0 or board[r][c - 1] == "."):
                ret += 1
            
    return ret