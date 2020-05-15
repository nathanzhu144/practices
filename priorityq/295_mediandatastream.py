# Nathan Zhu Wednesday August 7th, 2019, 2:38 pm.  EHS 55 John Street
#            May 4th, 2020, 11:52 pm, Stockton, CA, COVID-19, just finished 376 final 5 days ago.  Meera's bday yesterday
# Leetcode 295 | hard | not too bad
# Category: Priority Queue
# Runtime : Overall NlogN,
#           But benefit here is that you can find the median without recomputing 
#           a bunch of times.
#
# I've done this problem in a 281 project.  The intuition is clear on this one.
# 

import heapq
# shorter iml
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.big = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.small or -self.small[0] >= num:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)
            
        while len(self.small) - len(self.big) > 1:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        while len(self.big) > len(self.small) > 0:
            heapq.heappush(self.small, -heapq.heappop(self.big))
            
            

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.big):
            return (-self.small[0] + self.big[0]) / 2.0
        else:
            return -self.small[0]

# longer old impl w comments
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # If there is an odd number of elements, smaller has an extra one.

        # store the small half, top is the largest in the small part
        # store the large half, top is the smallest in the large part
        self.smaller = []  # A, max heap, structured with -1
        self.bigger = []   # B, min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.smaller:
            heapq.heappush(self.smaller, num * -1)
            return

        # If num <= maximal element on smaller (max heap), we push it 
        # into self.smaller
        #
        # If num > maximal element on smaller (max heap), we push it
        # onto self.bigger
        if num <= -1 * self.smaller[0]:
            heapq.heappush(self.smaller, num * -1)
        else:
            heapq.heappush(self.bigger, num)

        # If smaller's size is larger than len(self.bigger) + 1, 
        # smaller is too big, push biggest element of smaller onto bigger
        #
        # If bigger's size is larger than smaller, 
        # bigger is too big, push biggest element of bigger on smaller.
        # 
        # While or if both work here, since loop should only run once
        while len(self.smaller) > len(self.bigger) + 1:
            heapq.heappush(self.bigger, -1 * heapq.heappop(self.smaller))
        while len(self.bigger) > len(self.smaller):
            heapq.heappush(self.smaller, -1 * heapq.heappop(self.bigger))
        
    def findMedian(self):
        """
        :rtype: float
        """
        # If len(smaller) == 1 + len(bigger), median is on top of smaller
        # If len(smaller) == len(bigger), median is average of max of smaller and min of bigger.
        if len(self.smaller) > len(self.bigger): return -self.smaller[0]
        else: return (-self.smaller[0] + self.bigger[0]) / 2.0
