# Nathan Zhu August 27th, 2019, 2:09 pm 
# Leetcode 1066 | medium | medium
# Category: Backtracking
# Done in real-time in a "Google on-site interview", 1 hour 59 min spent for 2 hour interview
# Not sure what rating was


# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
# We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
# Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.


def assignBikes(workers, bikes):
    """
    :type workers: List[List[int]]
    :type bikes: List[List[int]]
    :rtype: int
    """

    def calc_dist(worker, bike):
        return abs(worker[0][0] - bike[1][0]) + abs(worker[0][1] - bike[1][1])
    
    def helper(left_bikes, curr_worker, mem):
        key = (curr_worker, tuple(left_bikes))
        if key in mem: return mem[key]
        
        if curr_worker == len(workers): return 0
        
        min_dist = float('inf')
        for i in range(len(left_bikes)):
            if left_bikes[i] == 0:
                left_bikes[i] = 1
                
                wx, wy = workers[curr_worker]
                bx, by = bikes[i]
                min_dist = min(min_dist, abs(wx - bx) + abs(wy - by) + helper(left_bikes, curr_worker + 1, mem))
                
                left_bikes[i] = 0
                
        mem[key] = min_dist
        return min_dist
        
    return helper([0 for i in range(len(bikes))], 0, dict())