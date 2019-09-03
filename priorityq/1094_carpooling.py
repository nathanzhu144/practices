# Nathan Zhu August 30th, 2019 1:06 pm
# Leetcodee 1094 | medium | medium
# Category: Sorted intervals.
#
# Apple- Phone Interview
# Your interview score of 3.94/10 beats 34% of all users.
# Time Spent: 1 hour 13 minutes 2 seconds
# Time Allotted: 1 hour 30 minutes

# Question:
# You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only 
# drives east (ie. it cannot turn around and drive west.)

# Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about
# the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  
# The locations are given as the number of kilometers due east from your vehicle's initial location.

# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false


class Trip(object):
    def __init__(self, passengers, start, end):
        self.passengers = passengers
        self.start = start
        self.end = end


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        alltrips = []

        for passengers, start, end in trips:
            alltrips.append(Trip(passengers, start, end))

        alltrips.sort(key=lambda x: x.start)

        currload = 0
        inprogtrips = []
        for trip in alltrips:
            removed = []
            for inprogtrip in inprogtrips:
                if inprogtrip.end <= trip.start:
                    currload -= inprogtrip.passengers
                    removed.append(inprogtrip)
            for remove in removed:
                inprogtrips.remove(remove)

            inprogtrips.append(trip)
            currload += trip.passengers
            if currload > capacity: return False

        return Trues