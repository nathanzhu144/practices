# Nathan Zhu May 2nd, 2020. Done during weekly conctest 182, placed top 400.  Amazing.
# Leetcode 1436 | easy | EZ
# 
# I finished the first 3 questions in the contest after spending ~29 min
# This question took me another 40ish min.  
# I originally wrote a N^2 soln and from intuition reduced it to O(N)
# with a sliding window and a monotonic queue.  I was so damn proud of myself
# for this one, like so damn proud.  This contest has been prob one of the highlights
# of 2020.
#
# Also, I crushed the hard one on this one with a "genius" idea from merging 
# k-sorted linked lists.  I was so impressed.


import collections
def destCity(self, paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    graph = collections.defaultdict(list)
    start = None
    for a, b in paths:
        start = a
        graph[a].append(b)
        
    def dfs(node):
        if node not in graph: return node
        # this for loop makes no sense lmao, can just return dfs(neigh)
        for neigh in graph[node]:
            return dfs(neigh)
            
    
    curr = dfs(start)
    return curr