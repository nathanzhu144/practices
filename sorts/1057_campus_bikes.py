# Nathan Zhu August 28th, 2019, 3:25 am
# Leetcode 1057 | medium | not easy
# Google- On-Site Interview
# Your interview score of 4.93/10 beats 63% of all users.
# Time Spent: 1 hour 27 minutes 26 seconds
# Time Allotted: 2 hours

# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 
# 2D coordinate on this grid.

# Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike)
# pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are 
# multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index;
# if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process 
# until there are no available workers.

# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

# Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

def assignBikes(self, workers, bikes):
    """
    :type workers: List[List[int]]
    :type bikes: List[List[int]]
    :rtype: List[int]
    """
    # Range of Manhattan distances for points [i, j], where i and j are bounded by 1000 is 2000.
    # We want each element of bucket to be a list of [workeridx, bikeidx]
    buckets = [[] for i in range(2001)]  
    for w in range(len(workers)):
        for b in range(len(bikes)):
            dist = abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
            buckets[dist].append([w, b])
            
    # Ret is a list of [worker, assigned bike]
    ret = [-1] * len(workers)
    assigned_bikes = set()
    assigned_people = set()
    
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            # If we haven't used this person and this bike before, we use this combination.
            if buckets[i][j][0] not in assigned_people and buckets[i][j][1] not in assigned_bikes:
                assigned_people.add(buckets[i][j][0])
                assigned_bikes.add(buckets[i][j][1])
                ret[buckets[i][j][0]] = buckets[i][j][1]
                
    return ret
                
                