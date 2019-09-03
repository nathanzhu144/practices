# Nathan Zhu Thursday 12:48 am, August 22nd, 2019
# Leetcode 1046 | easy | EZ
# 
# Category: priority queue
# https://leetcode.com/discuss/interview-question/344677/Amazon-or-Online-Assessment-2019-or-Min-Cost-to-Connect-Ropes
# 
# This is basically same question as min cost to connect ropes in Amazon OA for 2019.  
# Amazon OA has a bunch of ropes with lengths. Cost of connecting 2 ropes is sum of their lengths.  So, greedy soln is best, connect
# two smallest ropes, then next two smallest ... until you have one rope.
#

def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    pq = [-1 * i for i in stones]
    h   eapq.heapify(pq)
    
    while len(pq) > 1:
        firstrock = heapq.heappop(pq) * -1
        secondrock = heapq.heappop(pq) * -1
        
        if firstrock != secondrock:
            heapq.heappush(pq, -1 * (firstrock - secondrock))
            
    return 0 if not pq else -pq[0]