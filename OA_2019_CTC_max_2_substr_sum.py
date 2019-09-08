# Nathan Zhu August 5th, 2019 3:00 pm
# Category:  Interval, DP, pre-sum arr
#
# This was in the OA for Chicago trading.  3 hour time limit.
#
# Given A, an array of numbers, we want to find two subarrays of length Y and length Z.  We want to maximize the sum of these two subarrays,
# and they cannot overlap.

# Algorithm:
# Make presum array
# Find all intervals of size Y, calculate sum for each one using presum arr
# Find all intervals of size Z, calculate sum for each one using presum arr
# 
# Loop thru all these intervals, and if these two intervals don't overlap see if it is biggest so far.

import collections


def solution(A, Y, Z):
    # Not possible
    if Y + Z > len(A): return -1

    # Note that start and end are inclusive
    Interval = collections.namedtuple("Interval", "start end totsum")
    
    # Do two intervals overlap?
    # Returns False if they don't overlap,
    # returns True if they do overlap
    def overlap(int1, int2):
        return int1.start <= int2.end and int2.start <= int1.end
        
    # Calculating a presum for faster interval sum calculations
    presum = A[:]
    for i in range(len(presum)):
        if i - 1 >= 0: presum[i] = presum[i - 1] + A[i]
    
    # Processing length Y
    i1, i2 = [], []
    i = 0
    while Y > 0 and i + Y <= len(A):
        distance = 0
        if i == 0: distance = presum[i + Y - 1]
        else: distance = presum[i + Y - 1] - presum[i - 1]
        
        i1.append(Interval(i, i + Y - 1, distance))
        i += 1
        
    # Processing length Z
    i = 0
    while Z > 0 and i + Z <= len(A):
        distance = 0
        if i == 0: distance = presum[i + Z - 1]
        else: distance = presum[i + Z - 1] - presum[i - 1]
        
        i2.append(Interval(i, i + Z - 1, distance))
        i += 1
        
    ret = 0
    if not i1 and not i2: return 0
    elif not i1 and i2: return max([i.totsum for i in i2])
    elif not i2 and i1: return max([i.totsum for i in i1])
    
    for i in range(len(i1)):
        for j in range(len(i2)):
            int1, int2 = i1[i], i2[j]
            if overlap(int1, int2): continue
            
            # we now know they don't overlap
            currsum = int1.totsum + int2.totsum
            ret = max(ret, currsum)
    return ret