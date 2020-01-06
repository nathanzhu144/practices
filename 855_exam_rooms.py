# Nathan Zhu Thursday 11:50 pm January 2nd 2019
# Leetcode 855 | medium | pretty hard
# Category: intervals / heap
#
# We always care about the position where the seat is as far away as possible.
# 
# Seats: 0  1  2  3  4  5
#        
# 1st  : S  -  -  -  -  -
# 2nd  : S  -  -  -  -  S
# 3rd  : S  -  S  -  -  S  
# 4th  : S  S  S  -  -  S   (all are 1 spot away from another student, so choose lowest idx)

# One way of modelling the student is with intervals, with the initial interval being [-1, N], both are boundaries.
# The -1, N system tells us whether we can simply take position 0 or position N - 1 before going with abs(x - y) // 2
# 
import heapq
import collections

class ExamRoom(object):
    
    # The negative sign in front of all the distances is to ensure that the python min heap works properly.
    def dist(self, x, y):
        if x == -1: return -y
        elif y == self.N: return -(self.N - 1 - x)
        else: return  -(abs(x - y) // 2)

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.pq = []
        heapq.heappush(self.pq, (self.dist(-1, N), -1, N))
        
    # LogN time
    # We choose the seat with the longest dist away
    # We then split this interval into two and push them back onto the heap.
    def seat(self):
        """
        :rtype: int
        """
        _, x, y = heapq.heappop(self.pq)
        ret = 0
        if x == -1: ret = 0
        elif y == self.N: ret = self.N - 1
        else: ret = (x + y) // 2
            
        heapq.heappush(self.pq, (self.dist(x, ret), x, ret))
        heapq.heappush(self.pq, (self.dist(ret, y), ret, y))
        
        return ret

    # O(N) time
    # We know that given that this seat is being vacated, there exist two intervals, one which 
    # ends at this seat and one which starts at this seat.  We find them in O(N) time, and then merge the two, and push
    # that new merged interval back into heap.
    #
    # Removing the two intervals breaks heap invariant, so heapify must be called.
    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        left, right = None, None
        for interval in self.pq:
            if interval[1] == p: right = interval
            if interval[2] == p: left = interval
            if left and right: break
                
        self.pq.remove(left)
        self.pq.remove(right)
        heapq.heapify(self.pq)
        heapq.heappush(self.pq, (self.dist(left[1], right[2]), left[1], right[2]))
                