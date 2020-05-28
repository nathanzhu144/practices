# Nathan Zhu  Wednesday May 21st, 2020 11:53 pm, Finished 3rd day of work at Salesforce!
# LEetcode 1425 | hard | hard
# Category; PQ
# Naive DP is N^2
# This sol nis NlogK
# There is a O(N) monotonic queue soln

import heapq
def constrainedSubsetSum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    N = len(nums)
    ret = nums[0]
    pq = [(-nums[0], 0)]
    
    for i in range(1, N):
        min_prev_consider = i - k
        while pq[0][1] < min_prev_consider: heapq.heappop(pq)
            
        curr = max(nums[i], nums[i] - pq[0][0])
        heapq.heappush(pq, (-curr, i))
        ret = max(curr, ret)
        
    return ret
        