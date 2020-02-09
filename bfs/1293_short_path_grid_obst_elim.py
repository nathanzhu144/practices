
def shortestPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: int
    """
    # Invariants:
    # If something is in the Q, we CAN visit it, as in we have enough k to get there.
    # We only re-visit a node, if we can get to there with a smaller k value.
    
    visited = dict()
    q = [(0, 0, k)]   # row, col, k
    R, C = len(grid), len(grid[0])
    
    ret = 0
    while q:
        newq = []
        for r, c, newk in q:
            if r == R - 1 and c == C - 1: return ret
            visited[(r, c)] = newk
            if grid[r][c] == 1: newk -= 1
                
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                newr, newc = r + dr, c + dc
                if 0 <= newr < R and 0 <= newc < C and ((newr, newc) not in visited or newk < visited[(newr, newc)]):
                    if k == 0 and grid[newr][newc] == 1: continue
                    newq.append((newr, newc, newk))
        ret += 1
        q = newq
        
    return -1

if __name__ == "__main__":
    shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1)