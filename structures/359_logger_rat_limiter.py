# Nathan Zhu August 28th, 2019 3:24 am
# Category: System design
# Google- On-Site Interview
# Your interview score of 4.93/10 beats 63% of all users.
# Time Spent: 1 hour 27 minutes 26 seconds
# Time Allotted: 2 hours

# Given a message and a timestamp (in seconds granularity), return true if the message should be 
# printed in the given timestamp, otherwise returns false.
# 
# It is possible that several messages arrive roughly at the same time.


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tenmin = collections.deque([])

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        
        while self.tenmin and timestamp - self.tenmin[-1][0] >= 10:
            self.tenmin.pop()
            
        for i in range(len(self.tenmin)):
            if self.tenmin[i][1] == message:
                return False
            
        self.tenmin.appendleft((timestamp, message))
        return True
            
        