# Nathan Zhu May 2nd, 2020. Done during weekly conctest 182, placed top 400.  Amazing.
# Leetcode 1439 | hard | Damn cool, cracked this one basically immediately
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
import heapq
import collections

def kthSmallest(mat, k):
    """
    :type mat: List[List[int]]
    :type k: int
    :rtype: int
    """
    R, C = len(mat), len(mat[0])
    
    start = [mat[r][0] for r in range(R)]
    
    pq = [(sum(start), [0] * R)]
    lastsum = None
    visited = set()
    while k:
        lastsum, cols = heapq.heappop(pq)
        curr = "".join(map(str,cols))
        if curr in visited: continue
        visited.add(curr)
        
        for i, col in enumerate(cols):
            if col + 1 >= C: continue
            heapq.heappush(pq, (lastsum - mat[i][col] + mat[i][col + 1], cols[:i] + [col + 1] + cols[i + 1:]))
        k -= 1
    return lastsum
            