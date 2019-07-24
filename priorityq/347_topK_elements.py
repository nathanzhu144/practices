# Nathan Zhu Tuesday July 23rd, 2019, Amex Building, Floor 36.
# Leetcode 347 | medium | medium
# Category: pq
# Runtime: NlogK
# 

def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    c = collections.Counter(nums)
    heap = []
    for key in c:
        heapq.heappush(heap, (c[key], key))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for occurences, num in heap]