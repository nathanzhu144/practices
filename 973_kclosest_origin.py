
# This solution is nlogk, where k <= N
# This solution can deal with real-time data.  WE don't need to have all the data right now
# in order to use this solution.
#
def kClosest(self, points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    h = []
    for p in points:
        heapq.heappush(h, (-1 * (p[0] * p[0] + p[1] * p[1]), p))
        if len(h) > K: heapq.heappop(h)
    
    return [point for distance, point in heapq.nlargest(K, h)]