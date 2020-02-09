# Nathan Zhu Tuesday Jan 21st, 2019 8:01 am Shapiro Library, 4th floor where birds usually are, but I don't hear the birds anymore.  Too cold today?
# Leetcode 286 | medium | damn genius man
# I love this solution.
# Naive BFS is N^4 worst case, as you do a N^2 traversal N^2 times.  *assuming square matrix*
# This method is N^2 worst case, as you do a BFS one time.

# Idea: 
# Push all gates into queue first. Then for each gate update its neighbor cells and push them to the queue.
# Repeating above steps until there is nothing left in the queue.

def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """
    if not rooms or not rooms[0]: return
    
    q = collections.deque([])
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    R, C = len(rooms), len(rooms[0])
    
    # Finding all gates and adding them to the queue
    for r in range(R):
        for c in range(C):
            if rooms[r][c] == 0: q.append((r, c))
    
    # If a gate ever sees a infinite in our BFS, we know that is the closest path to that infinite.
    # Mark it, and put it back into BFS
    while q:
        r, c = q.pop()
        for dr, dc in moves:
            newr, newc = r + dr, c + dc
            if 0 <= newr < R and 0 <= newc < C and rooms[newr][newc] == 2 ** 31 - 1:
                rooms[newr][newc] = rooms[r][c] + 1
                q.appendleft((newr, newc))
                