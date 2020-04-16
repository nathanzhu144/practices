# Nathan Zhu Saturday, April 11th, 2020. 4:44 pm, Stockton, CA.  Discovered some big veitchii pitchers today.
# Leetcode 656 | hard | not that hard?  a bit tricky
# Category: DP / Djikstra
# Simple N^2 DP algorithm.
# 
# 

import heapq
def cheapestJump(A, B):
    """
    :type A: List[int]
    :type B: int
    :rtype: List[int]
    """
    N = len(A)
    
    if N == 0: return True
    if A[0] == -1: return False
    
    dp, path = [float('inf')] * N, [-1] * N
    dp[N - 1] = A[N -  1]
    for i in range(N - 2, -1, -1):
        if A[i] == -1: continue
        for j in range(i + 1, min(N, i + B + 1)):
            if A[j] == -1: continue
                
            # Notice that since we only alter the path if we get 
            # a smaller number, we priority earlier paths.
            if A[i] + dp[j] < dp[i]:
                dp[i] = A[i] + dp[j]
                path[i] = j
                
    if dp[0] == float('inf'): return []
    res = []
    k = 0

    # Note that last idx in path is -1
    while k != -1:
        res.append(k + 1)
        k = path[k]
        
    return res



# This solution works if all the jump costs are positive, which they are in this question.
#                 and we don't necessarily care about the lexicographically smaller path (which we do).
# The problem I had with a PQ was I was faced with either extracting all paths of minimum length (which is possible)
# but kinda not crisp to write or generating the first one (which was kinda hard).
# Overall, the DP one is easier if we want the lexicographically smaller path.
#
def cheapestJumpPQ(A, B):
    """
    :type A: List[int]
    :type B: int
    :rtype: List[int]
    """
    N = len(A)
    visited = set()
    
    if N == 0: return True
    if A[0] == -1: return False
    
    pq = [(A[0], [0], 0)]
    while pq:
        cost, currpath, cidx = heapq.heappop(pq)
        if cidx == N - 1: return [1 + val for val in currpath]
        
        for i in range(1, B + 1):
            if cidx + i >= N: break
            newidx = i + cidx
            
            if newidx in visited or A[newidx] == -1: continue
            visited.add(newidx)
            heapq.heappush(pq, (cost + A[newidx], currpath + [newidx], newidx))
        
    return []
    
if __name__ == "__main__":
    print(cheapestJump([1,2,4,-1,2], 2))