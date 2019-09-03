# Nathan Zhu August 29th, 2019 12:58 am
# Leetcode 857 | hard | HARD
#
# Google- On-Site Interview
# Your interview score of 6.04/10 beats 87% of all users.
# Time Spent: 1 hour 30 minutes 12 seconds
# Time Allotted: 2 hours

# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

# Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers,
# we must pay them according to the following rules:

# Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage expectation.
# Return the least amount of money needed to form a paid group satisfying the above conditions.


def mincostToHireWorkers(quality, wage, K):
    """
    :type quality: List[int]
    :type wage: List[int]
    :type K: int
    :rtype: float
    """
    # 1. We sort from smallest to biggest wage / quality.  
    workers = sorted([(float(wage[i]) / quality[i], quality[i]) for i in range(len(quality))])
    
    totq = 0
    heap = []
    ret = float('inf')
    
    for i in range(len(workers)):
        ratio, quality = workers[i]
        totq += quality
        heapq.heappush(heap, -quality)
        
        if len(heap) > K: totq += heapq.heappop(heap)
        if len(heap) == K: ret = min(ret, ratio * totq)
            
    return ret