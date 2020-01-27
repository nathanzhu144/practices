# Nathan Zhu August 31st, 2019 2:24 pm
# Leetcode 346 | easy | EZ
# Category: System design
# Random Set- Online Assessment
# Your interview score of 4.60/10 beats 48% of all users.
# Note: You can use a circular buffer to implement this one, but didn't use it

# class MovingAverage(object):

#     def __init__(self, size):
#         """
#         Initialize your data structure here.
#         :type size: int
#         """
#         self.tot = 0
#         self.count = 0
#         self.size = size
#         self.prefixsum = collections.deque([])
        
#     def next(self, val):
#         """
#         :type val: int
#         :rtype: float
#         """
        
#         if self.prefixsum:
#             self.prefixsum.append(val + self.prefixsum[-1])
            
#             if len(self.prefixsum) > self.size + 1: self.prefixsum.popleft()
                
#             if len(self.prefixsum) == self.size + 1: return (self.prefixsum[-1] - self.prefixsum[0]) / float(self.size)
#             else: return self.prefixsum[-1] / float(len(self.prefixsum))
#         else:
#             self.prefixsum.append(val)
#             return val
        
# This one is still O(1) team is easier to implement

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.arr = collections.deque([])
        self.k = size
        self.curr = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.curr += val
        self.arr.append(val)
        if len(self.arr) > self.k: 
            tmp = self.arr.popleft()
            self.curr -= tmp
            
        return self.curr / (1.0 * len(self.arr))