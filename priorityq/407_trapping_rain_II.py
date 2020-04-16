# Nathan Zhu April 11th, 2020 10:50 am
# Leetcode 407 | hard | hard
# Category: Priority queue

# Originally, I was doing a strategy where I looked for the highest wall on all 4 sides, and took the minimum of them.
# I did this by generating four grids, each finding the maximum height up to this point from bottom-up, top-down, left-right, and 
# right-left.
#
#   This strat fails on this grid:
# 
#   12 13 1  12
#   13 [4] 13 12
#   13 8  10 12
#   12 13 12 12
#   13 13 13 13
# 
#   In this case, the sweeping will fail for the [4].  The sweep will see the water level as 13, but because water will flow 
#   through the 8, 10, 12, this would fail, making the max height actually 12.  This strat is not generalizable to the 2d case.
#
#
# So, the new strategy is to put all the surrounding boxes into a priority queue, and only removing the smallest heights.
# We then keep taking the smallest hiehg in the PQ.  Everytime we remove something the PQ, we update our max height.  If any new
# square is not visited, and the max height is greater than the grid square, we have a positive water value.
import heapq
def trapRainWater(grid):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    R, C = len(grid), len(grid[0])
    pq = []
    
    # Touched means the grid is in the pq or has been in pq
    touched = set()
    
    for r in range(R):
        for c in range(C):
            key = (r, c)
            if (r == 0 or c == 0 or r == R - 1 or c == C - 1) and key not in touched: 
                heapq.heappush(pq, (grid[r][c], key))
                touched.add(key)
    
    ret = 0
    global_m = float('-inf')
    while pq:
        curr, loc = heapq.heappop(pq)
        r, c = loc
        global_m = max(curr, global_m)
        
        
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            newr, newc = r + dr, c + dc
            new_move = (newr, newc)
            
            if not (0 <= newr < R and 0 <= newc < C) or new_move in touched: continue
            
            ret += max(0, global_m - grid[newr][newc])
            heapq.heappush(pq, (grid[newr][newc], new_move))
            touched.add(new_move)
            
    return ret

if __name__ == "__main__":
    print(trapRainWater(
        [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
        ]
        ))