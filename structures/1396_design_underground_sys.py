# Nathan Zhu May 28th, 2020. 10:00 pm, COVID-19, Foundry, in Leetcode contest
# Leetcode 1396 | medium | not bad
# Category: Design
# 

import collections

class UndergroundSystem(object):

    def __init__(self):
        self.last_checkin = dict()                              # maps id -> (staton, time)
        self.station_tot_time = collections.defaultdict(int)  # Maps edge -> total time trav between
        self.station_visits = collections.defaultdict(int)    # Maps edge -> total trips

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.last_checkin[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        pr = (self.last_checkin[id][0], stationName) 
        self.station_tot_time[pr] += t - self.last_checkin[id][1]
        self.station_visits[pr] += 1
        

    def getAverageTime(self, s, e):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        pr = (s, e)
        return self.station_tot_time[pr] / (1.0 * self.station_visits[pr])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)