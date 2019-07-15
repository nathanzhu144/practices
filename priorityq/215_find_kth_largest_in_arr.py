# Nathan Zhu, Monday July 1st, 2019 American Express Building 11:17 am
# Leetcode 215 | medium | easy? not too bad

import heapq

# Overall is KLogK instead of NlogN
# Note: Python default is a min heap, not a max heap, so popping returns minimum element.
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    heap = list()
    # Pushing into heap should be a logK operation, heap is of len(k) at largest
    # we do it N times, so overall this is N(logK) where K <= N
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k: heapq.heappop(heap)
    
    # I believe that this is a K(logK) operation.
    return heapq.nlargest(k, heap)[k - 1]

# Since python default is a min heap, a hack is to negate all numbers in heap...
def findKthSmallest(nums, k):
    heap = list()

    for num in nums:
        heapq.heappush(heap, -1 * num)
        if len(heap) > k: heapq.heappop(heap)
        
    return -1 * heapq.nlargest(k, heap)[k - 1]
            

if __name__ == "__main__":
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))