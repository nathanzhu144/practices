# Nathan Zhu August 31th, 2019 10:45 
# Google- On-Site Interview
# Your interview score of 4.57/10 beats 76% of all users.
# Time Spent: 1 hour 59 minutes 25 seconds
# Time Allotted: 2 hours

# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
# What is the largest possible number of moves we can make?

# Example 1:

# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5



def removeStones(self, stones):
    visited = set()
    all_stones = set([tuple(stone) for stone in stones])
    
    def helper(row, col):
        if (row, col) in visited: return
        visited.add((row, col))
        
        for s2 in stones:
            if tuple(s2) not in visited and s2[0] == row or s2[1] == col: 
                helper(s2[0], s2[1])
    ret = 0  
    for row, col in stones:
        if (row, col) not in visited:
            helper(row, col)
            ret += 1
            
    return len(stones) - ret
        

#  This soln works, but TLE.  Does backtracking to solve the problem, dumb doesn't realize insight.
#  
#     def removeStones(self, stones):
#         """
#         :type stones: List[List[int]]
#         :rtype: int
#         """
#         maximal = [0]
#         def helper(rows, cols, moves, visited, nummoves):
#             ret = 0
#             maximal[0] = max(maximal[0], nummoves)

#             for move in moves:
#                 if move in visited: continue
#                 mrow, mcol = move
                
#                 for key, val in rows.items():
#                     remainingmoves = [m for m in val if m not in visited]
#                     if len(remainingmoves) < 2: continue
                        
#                     for move in remainingmoves:
#                         visited.add(move)
#                         helper(rows, cols, moves, visited, nummoves + 1)
#                         visited.remove(move)
                
#                 for key, val in cols.items():
#                     remainingmoves = [m for m in val if m not in visited]
#                     if len(remainingmoves) < 2: continue
                    
#                     for move in remainingmoves:
#                         visited.add(move)
#                         helper(rows, cols, moves, visited, nummoves + 1)
#                         visited.remove(move)
                        
#         moves = [tuple(move) for move in stones]
#         rows, cols = collections.defaultdict(list), collections.defaultdict(list)
        
#         for m in moves:
#             r, c = m
#             rows[r].append(m)
#             cols[c].append(m)
        
#         helper(rows, cols, moves, set(), 0)
#         return maximal[0]