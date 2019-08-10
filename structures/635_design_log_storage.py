# Nathan Zhu EHS 55, August 4th, 2019, 7:00 pm.
# Leetcode 635 | medium | medium?
# 
# The solution to this is kinda stupid.  Retreive is O(N), and can be shaved down to O(logN)
# with the right data structures. But, right now put is O(1), and inserting into a regular list
# would make put O(N)
#
# 
# Question 
# 
# You are given several logs that each log contains a unique id and timestamp. Timestamp is a string
# that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59.
# All domains are zero-padded decimal numbers.
# Design a log storage system to implement the following functions:

# void Put(int id, string timestamp): Given a log's unique id and timestamp, 
# store the log in your storage system.

# int[] Retrieve(String start, String end, String granularity): Return the id of 
# logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp

class LogSystem(object):
    # You can store logs with a timestamp 
    def __init__(self):
        # self.g maps from granularity of search -> end splice index for timestamp
        self.times = []
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        self.times.append([timestamp, id])
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        idx = self.g[gra]
        start, end = s[:idx], e[:idx]
        
        return [i for time, i in self.times if start <= time[:idx] <= end]