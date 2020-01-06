# Nathan Zhu 7:24 am January 2nd, 2019. 
# Leetcode 957 | medium | hard
# This question masquerades as a simpler game of life, but is actually an application of the pidgeonhole principle.
# There are only 8 squares, 6 of which can be a 0 or 1 after a later iteration.
# Therefore, there are only 2^6 states.  So, when N is massive, like 100,000, we definitely have at least one cycle.

# The line N %= seen[key] - N is simple.
# Just write an example.
#
# arr  N
# A   10        
# B   9
# C   8
# D   7
# A   6        <- seen again, N is 6 initially, then N = 6 % (10 - 6) = 2.  
# B   5
# C   4
# D   3
# A   2        <- now N is 2, at the same position A, and runs the rest of the positions.
# B   1

def prisonAfterNDays(self, cells, N):
    """
    :type cells: List[int]
    :type N: int
    :rtype: List[int]
    """
    def next_day(cells):
        ret = [0] * len(cells)
        
        for i in range(1, len(cells) - 1):
            ret[i] = int(cells[i - 1] == cells[i + 1])
        return ret
    
    seen = dict()
    while N > 0:
        key = tuple(cells)
        if key in seen:
            N %= seen[key] - N
        seen[key] = N
        
        if N >= 1:
            cells = next_day(cells)
            N -= 1
        
        
    return cells
            
            
