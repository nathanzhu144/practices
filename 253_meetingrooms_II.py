# Nathan Zhu Sunday July 21st, 2019.  Amex Building 36th, floor in empty conf room.  I think Michael and Zion are getting lunch uptown rn?
# Leetcode 253 | medium | medium
# Category: Intervals

# Insight:
#  This is a two pointer problem (greedy solution).
#  Sort start and end intervals. Take two pointers, one for start time and one for end time. 
#  if the start interval is less than the end interval increment the room counter since we 
#  would need a extra room, else decrement the count since we have freed up the room.
#
#  What the algorithm is doing is checking how many meetings begin before the earliest-ended meeting ends. 
#  If, for instance, 3 meetings have started before the earliest possible meeting end, than we need 3 rooms.
#  Sorting the arrays helps in two things: first of all you can easily get the earliest meetings end time, 
#  and secondly, it allows you to start looking for meetings ends only from next element in the ends array 
#  when you find some meeting start that is after the current end, because all other meeting ends before the
#  current in the sorted array will also be before the current meeting start. So you just have to run 1 time over each array.
#
#
# Question:
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# find the minimum number of conference rooms required.

# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1


# 1. Sort by front
def meeting_rooms_II(intervals):
    start, finish = [], []
    for s, f in intervals:
        start.append(s)
        finish.append(f)

    start = sorted(start)
    finish = sorted(finish)
    ret, curr_rooms = 0, 0
    start_i, finish_i = 0, 0

    while start_i < len(intervals):
        if start[start_i] < finish[finish_i]:
            curr_rooms += 1
            start_i += 1
            ret = max(ret, curr_rooms)
        elif start[start_i] > finish[finish_i]:
            curr_rooms -= 1
            finish_i += 1
        # if start[i] == finish[i], we do not need a new_room
        # but we don't lose a room, we simply increment both pointers
        else:
            start_i += 1
            finish_i += 1
    
    return ret

