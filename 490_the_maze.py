# Nathan Zhu December 29th, 2019 11:06 pm Santa Cruz hotel
# Leetcode 505 | medium | ez
# Category: BFS
# Classic bfs
# 

def hasPath(maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    R, C = len(maze), len(maze[0])
    visited = set()
    
    q = [start]
    while q:
        next_q = []
        for r, c in q:
            if (r, c) in visited: continue
            visited.add((r, c))
            
            if r == destination[0] and c == destination[1]: return True
            
            for dr, dc in dirs:
                newr, newc = r, c
                while 0 <= newr + dr < R and 0 <= newc + dc < C and maze[newr + dr][newc + dc] == 0:
                    newr += dr
                    newc += dc

                next_q.append((newr, newc))
        q = next_q
    return False
if __name__ == "__main__":
    hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4])