# Nathan Zhu August 30th, 2019 1:17 am
# Leetcode 855 | hard | HARD
# Category: priority queue 
# 
# Google- On-Site Interview
# Your interview score of 6.36/10 beats 87% of all users.
# Time Spent: 1 hour 23 minutes 49 seconds
# Time Allotted: 2 hours

# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there
# are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the 
# student sits at seat number 0.)



import heapq

class Interval(object):
    def __init__(self, start, end, N):
        self.start = start
        self.end = end
        self.distance = 0
        
        if start == -1:
            self.distance = end
        if end == N:
            self.distance = end - start - 1
        else:
            self.distance = abs(start - end) // 2
            
            

class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.pq = []
        first = Interval(-1, N, self.N)
        heapq.heappush(self.pq, (-first.distance, first.start, first))
        

    def seat(self):
        """
        :rtype: int
        """
        temp1, temp2, top = heapq.heappop(self.pq)
        seat = 0
        
        if top.start == -1: seat = 0
        elif top.end == self.N: seat = self.N - 1
        else: seat = (top.start + top.end) // 2
        
        newintervalleft = Interval(top.start, seat, self.N)
        newintervalright = Interval(seat, top.end, self.N)
        heapq.heappush(self.pq, (-newintervalleft.distance, newintervalleft.start, newintervalleft))
        heapq.heappush(self.pq, (-newintervalright.distance, newintervalright.start, newintervalright))
        
        return seat
    

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        left, right = None, None
        for temp1, temp2, interv in self.pq:
            if interv.end == p: left = (temp1, temp2, interv)
            if interv.start == p: right = (temp1, temp2, interv)
            if left and right: break
                
        self.pq.remove(left)
        self.pq.remove(right)
        newinterv = Interval(left[2].start, right[2].end, self.N)
        self.pq.append((-newinterv.distance, newinterv.start, newinterv))
        heapq.heapify(self.pq)