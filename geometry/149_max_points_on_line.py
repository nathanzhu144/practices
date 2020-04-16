# Nathan Zhu April 14th, 2020. 
# Leetcode 149 | hard | kind hard
# Category: Math / geometry
# 

# Insight, if two lines share a point, if they have the same slope, they
# must be the same line.
#
# We can get two lines to share a point by fixing a point, and seeing out of all the other
# points how many have the same slope as this pair.  If so, that point must also be on the same line.
# 
# We handle points with the same slope with a duplicate counter.
import collections

def maxPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    

    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    ret = 0
    N = len(points)
    
    for i in range(N):
        dup = 1
        table = collections.defaultdict(int)
        for j in range(i + 1, N):
            if points[i] == points[j]: dup += 1
            else:
                dr = points[i][0] - points[j][0]
                dc = points[i][1] - points[j][1]
                g = gcd(dr, dc)
                
                table[str(dr / g) + " " + str(dc / g)] += 1
                
        ret = max(dup, ret)
        for key, val in table.items():
            ret = max(dup + val, ret)
            
    return ret