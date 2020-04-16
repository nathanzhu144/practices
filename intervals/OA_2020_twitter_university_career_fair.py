# Nathan Zhu Foundry Lofts Sunday Feb 2nd, 2020.  7:46 pm
# Leetcode n/a | ? | medium
# Category: Intervals, specifically greedy lecture hall scheduling.
#
# Given a list of arrival and duration times, which have the same length, and that only one event
# can occur at a time, what's max events we can accomodate?
#
# Arrival = [1, 3, 3, 5, 7]
# Duration = [2, 2, 1, 2, 1]

def maxEvents(arrival, duration):
    # Write your code here
    intervals = []

    for start, dur in zip(arrival, duration):
        intervals.append([start, start + dur])

    intervals.sort(key=lambda x: x[1])

    ret = []
    for start, end in intervals:
        if not ret or start >= ret[-1][-1]: ret.append([start, end])
    return len(ret)