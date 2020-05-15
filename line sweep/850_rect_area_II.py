# Nathan Zhu April 5th, 2020. 2:15 am, Stockton, CA.
# Leetcode 850 | hard | damn cool
# Category: Line sweep
# 
# Runtime: Is it N^2LogN?  WE do a NlogN sort up to N times.
# Combining the idea behind of merge intervals with a line sweep gives us a pretty elegant N^2 soln.
# 

import collections

def rectangleArea(self, rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: int
    """
    def get_overlap(intervals):
        if not intervals: return 0
        intervals = sorted(intervals)
        start, end = intervals[0][0], intervals[0][1]
        ret = end - start

        for s, e in intervals[1:]:
            if s >= end:
                end = e
                ret += (end - s)
            else:
                ret += max(0, e - end)
                end = max(end, e)
        return ret
    MOD = 10 ** 9 + 7
    table = collections.defaultdict(list)

    for x1, y1, x2, y2 in rectangles:
        table[y1].append((True, x1, x2))
        table[y2].append((False, x1, x2))

    intervals = list()
    y_to_event = sorted(table.items())
    last_y, last_merge_length, ret = 0, 0, 0

    for y, changes in y_to_event:
        ret += (y - last_y) * last_merge_length
        for add, start, end in changes:
            if not add: intervals.remove((start, end))
            else: intervals.append((start, end))

        last_y, last_merge_length = y, get_overlap(intervals)

    return ret % MOD