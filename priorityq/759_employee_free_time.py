# Nathan Zhu Nov 27th, 2019 12:31 pm
# Leetcode 759 | hard | is it really hard?
# Category: PQ, Intervals
# 
# Note: Most people don't take advantage of the fact that each of the people's 
#       intervals are sorted, leading to NlogN solns, whereas this is NlogK, where
#       k is number of people and N is length of longest list.
# 
import collections
import heapq

class Interval:
    def __init__ (self, start, end):
        self.start = start
        self.end = end


def employeeFreeTime(schedule):
    """
    :type schedule: list<list<Interval>>
    :rtype: list<Interval>
    """
    # Essentially, we have a min PQ of iterators, sorted by the start time 
    # of the interval the iterator is pointed at.
    heap = []
    Interv = collections.namedtuple("Interv", ["start", "arr", "index"])
    for i in range(len(schedule)):
        heapq.heappush(heap, Interv(schedule[i][0].start, schedule[i], 0))
    
    
    ret = []
    # old_end keeps track of largest time we have booked
    # Since we are looking at all the intervals in sorted order, if we 
    # ever see an interval starting after old_end, we know that [old_end, new_start]
    # is a free interval.
    old_end = heap[0].arr[0].start if len(heap) else None

    while heap:
        curr = heapq.heappop(heap)
        index = curr.index
        
        # We find free time.
        if curr.start > old_end:
            ret.append(Interval(old_end, curr.start))
            old_end = curr.arr[index].end
        # We might get a larger ending time.
        else:
            old_end = max(old_end, curr.arr[index].end)
        
        # If possible, we move the iterator to next element in list, 
        # modify comparator, and push back into list.
        if curr.index < len(curr.arr) - 1:
            heapq.heappush(heap, Interv(curr.arr[index + 1].start, curr.arr, index + 1))
        
    return ret

if __name__ == "__main__":
    employeeFreeTime([[Interval(0, 1), Interval, (6, 7)]])

