# Nathan Zhu Tuesday July 28th, 2020 11:37 pm, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  Met up with Katie, also Dara/Austin yesterday
#                                                          Kaushal has good hummingbird pics.
# Leetcode 1301 | hard | hardish
# Category: DP
# Runtime: N^2
# 

import collections

# The reason this problem can be done is that greed is good.
# Assuming the final path goes thru a square, we just need to return the global maximum of this square.  
# 
def pathsWithMaxScore(self, board):
    """
    :type board: List[str]
    :rtype: List[int]
    """
    N, MOD = len(board), 10 ** 9 + 7
    if not N: return [0, 0]  
    
    # [max_val, count]
    grid = [[[0, 0] for r in range(N + 1)] for c in range(N + 1)]
    grid[N - 1][N - 1] = [0, 1]
    for r in range(N - 1, -1, -1):
        for c in range(N - 1, -1, -1):
            # Don't add any values for start, end.
            if board[r][c] in "XS": continue
            
            # Look at bottom, left, bottomleft square. 
            # We are trying to find the greatest incoming value, and if there are ties, we 
            # combine the ways from both with addition.
            for dr, dc in (0, 1), (1, 0), (1, 1):
                oldr, oldc = dr + r, dc + c
                if grid[r][c][0] < grid[oldr][oldc][0]:
                    grid[r][c] = [grid[oldr][oldc][0], 0]
                if grid[r][c][0] == grid[oldr][oldc][0]:
                    grid[r][c][1] = (grid[oldr][oldc][1] + grid[r][c][1]) % MOD
            
            # Add value on if and only if square is not end square.
            if r or c: grid[r][c][0] += int(board[r][c])
                
    return grid[0][0] if grid[0][0][1] else [0, 0]

if __name__ == "__main__":
    print(pathsWithMaxScore(
        ["E12",
            "1X1",
            "21S"]))