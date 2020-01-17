# Nathan Zhu December 29th, 2019 11:06 pm Santa Cruz hotel
# Leetcode 505 | medium | medium
# Category: Priority queue / Djikstra

import heapq
def shortestDistance(maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
    """
    
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    R, C = len(maze), len(maze[0])
    
    prev_stops = {(start[0], start[1]) : 0}
    q = [(0, start[0], start[1])]
    
    while q:
        dist, r, c = heapq.heappop(q)
        if r == destination[0] and c == destination[1]: return dist
        
        for dr, dc in dirs:
            newdist = 0
            newr, newc = r, c
            while 0 <= newr + dr < R and 0 <= newc + dc < C and maze[newr + dr][newc + dc] == 0:
                newr += dr
                newc += dc
                newdist += 1
                
            newpos = (newr, newc)
            if newpos not in prev_stops or newdist < prev_stops[newpos]:
                prev_stops[newpos] = newdist
                heapq.heappush(q, (newdist + dist, newr, newc))
        
    return -1
                
                
                

if __name__ == "__main__":
    print(shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]))