#  Nathan Zhu 9:13 am, American Express Building
#  Leetcode 56 | medium | I thought was hard, until I realized the trick.
#  June 25th, 2019, sitting in a focus room on 36th floor, I'm nearly dry now
#
#  First, we sort all the intervals by starting time.
# 
#  For every new interval, we check whether it overlaps with the last one in
#  returned (if the end item of returned, has an end that is >= start of new interval)
#  If so, we merge the two. 
#  The ending of the interval at the end of returned is the maximum of the two endings.

def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    
    returned = []
    for i in sorted(intervals):
        if returned and returned[-1][1] >= i[0]:
            returned[-1][1] = max(returned[-1][1], i[1])
        else:
            returned.append(i)
            
    return returned