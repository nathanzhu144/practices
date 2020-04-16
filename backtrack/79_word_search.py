# Nathan Zhu Feb 16th, 2020.  Day after birthday, beem studying 376 today, reached like level 4k in gemcraft, good day.
#                             Talked to Ellen about 376 too.  She doesn't get reductions too well.
# Leetcode 79 | medium | easy
# Category: DFS / Backtracking



def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if not board or not board[0]: return False
    R, C = len(board), len(board[0])
    
    def find(word, r, c):
        if not word: return True
        if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[0]: return False
        
        board[r][c] = "*"
        ret = find(word[1:], r + 1, c) or find(word[1:], r, c + 1)or find(word[1:], r, c - 1) or find(word[1:], r - 1, c)
        board[r][c] = word[0]
        return ret
    
    for r in range(R):
        for c in range(C):
            if find(word, r, c): return True
            
    return False