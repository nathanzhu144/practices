# Nathan Zhu, Amex Building 36th floor, Just got back from Fun in the Sun 5:36 pm
# Leetcode 435 | medium | easy with insight
# Runtime: NLogN
# Problem:
# Given a collection of intervals, find the minimum number of intervals you need to 
# remove to make the rest of the intervals non-overlapping.
#
# Insight:
# This is the same problem as given a bunch of lectures with start and end times, how do
# we fit the most lectures in?
#
#  
# This is a variation of lecture hall scheduling. The optimal way to do
# lecture hall scheduling is to sort by start time from earliest end
# time to latest end time.  
#
# We start from choosing the interval with the earliest ending time.
# Then, we choose the interval with next earliest end time that is not 
# overlapping with the current interval.
#


def non_overlapping_intervals(intervals):
    end, cnt = float('-inf'), 0

    # At this point, we are guaranteed each successive interval has a later end time
    for i in sorted(intervals, key=lambda x: x[1]):
        # not-overlapping interval, we use this interval in lecture hall scheduling
        # we have equals cause if two intervals are touching, they still are not overlapping,
        if i[0] >= end:
            end = i[1]
        # we remove this interval, not used in lecture hall scheduling
        # we increment 1 bc we want to see minimum number of intervals we need to remove to
        # make all intervals non-overlapping
        else:
            cnt += 1
    return cnt