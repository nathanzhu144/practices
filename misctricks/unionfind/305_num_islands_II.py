# Nathan Zhu August 31st, 2019 2:24 am
# Leetcode 205 | hard | hard
# Category: Union find
# Your interview score of 3.21/10 beats 48% of all users.
# Time Spent: 1 hour 59 minutes 14 seconds
# Time Allotted: 2 hours


# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns 
# the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after 
# each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
# vertically. You may assume all four edges of the grid are all surrounded by water.

# Example:

# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]


class Union(object):
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0
    
    def add_island(self, p):
        if p in self.id: return
        self.id[p] = p
        self.size[p] = 1
        self.count += 1
        
    def find(self, i):
        if i != self.id[i]:
            self.id[i] = self.find(self.id[i])
        return self.id[i]

    
    def union(self, i, j):
        # Find ultimate parent.
        i, j = self.find(i), self.find(j)
        
        # If both belong to same subgraph, return, nothing to union
        if i == j: return
        
        # We want to guarantee i has smaller size than j, we 
        # are going to replace i with a pointer to j
        if self.size[i] > self.size[j]:
            i,j = j, i
            
        self.id[i] = j
        self.size[j] += self.size[i]
        self.count -= 1

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        islands = Union()
        
        for p in map(tuple, positions):
            islands.add_island(p)
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newx, newy = p[0] + dx, p[1] + dy
                if (newx, newy) in islands.id:
                    islands.union((newx, newy), p)
            
            ans.append(islands.count)
            
        return ans