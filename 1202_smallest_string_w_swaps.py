# Nathan Zhu 7:37 pm Christmas Day December 25th, 2019
# Leetcode 1202 | medium | ehh hard/medium
# Category: Union-find / DFS / misc-tricks
# Technically DFS and UF have same time complexity in this case, but I did UF.

# You are given a string s, and an array of pairs of indices in the
# string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# You can swap the characters at any pair of indices in the given pairs any number of times.
# Return the lexicographically smallest string that s can be changed to after using the swaps.
#
# Insights:
# 1. The core of the idea is that if (0, 1) is an exchange pair and (0, 2) is an exchange pair,
#     then any 2 in (0, 1, 2) can be exchanged.  I figured this one out on my own!
# 2. Then, we sort each of the subgraphs by lexicographical order of characters in that subgraph.
# 3. After this, we take the smallest character we can find depending on the subgraph it is in.


import collections

def smallestStringWithSwaps(s, pairs):
    """
    :type s: str
    :type pairs: List[List[int]]
    :rtype: str
    """
    class UF:
        def __init__(self, N):
            self.parent = list(range(N))
            
        def find(self, n):
            if self.parent[n] != n:
                self.parent[n] = self.find(self.parent[n])
            return self.parent[n]
            
        def union(self, a, b):
            if self.find(a) == self.find(b): return
            self.parent[self.find(a)] = self.parent[self.find(b)]
            
    U = UF(len(s))
    c = collections.defaultdict(list)
    ret = []
    
    for a, b in pairs:
        U.union(a, b)
        
    for i in range(len(s)):
        c[U.find(i)].append(s[i])
        
    for key in c: c[key].sort(reverse=True)
        
    for i in range(len(s)):
        ret.append(c[U.find(i)].pop())
        
    return "".join(ret)

smallestStringWithSwaps("dcabe", [[0,3],[1,2],[0,2]])