# Nathan Zhu August 26th, 2019 1:55 pm, Stockton California
# Leetcode 688 | medium | I think not too bad
# Category: DFS / DP
# 
# Done in real-time in a "Google phone interview"
# Rating was 5.19/10, beating 66% of all users.
# 

# General algo
# We go through all paths of length k until it goes off the board or it has moved k times.
# We record how many of those went off the board.
#
# num off board // total paths == percentage
#
#
# Ideas
# A nextsquare function -> curr square to a list of all neighbors
# 
# 
def knightProbability(self, N, K, r, c):
    """
    :type N: int
    :type K: int
    :type r: int
    :type c: int
    :rtype: float
    """
    
    def is_valid_pos(N, row, col):
        return row >= 0 and col >= 0 and row < N and col < N
    
    def get_neighbors(row, col):
        return [(row + drow, col + dcol) for drow, dcol in [(2, 1), (1, 2), (-2, -1), (-1, -2), (-2, 1), (1, -2), (2, -1), (-1, 2)]]
    
    def helper(row, col, K, mem):
        key = (row, col, K)
        if key in mem: return mem[key]
        
        if not is_valid_pos(N, row, col): return 0
        if K == 0 and is_valid_pos(N, row, col): return 1
        
        count = 0
        for newrow, newcol in get_neighbors(row, col):
            count += helper(newrow, newcol, K - 1, mem)
        
        mem[key] = count
        return mem[key]
            
    on_board = helper(r, c, K, dict())
    return on_board / float(8 ** K)