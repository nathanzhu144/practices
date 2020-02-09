# Nathan Zhu Jan 26th, 2020 Foundry Lofts 9:00 pm
# Leetcode 554 | medium | not bad
# Category: Misc tricks / hash table
# 
# Hash the x-vals of all of the bricks.
# 
def leastBricks(self, wall):
    """
    :type wall: List[List[int]]
    :rtype: int
    """
    if not wall: return 0
    # 1, 3, 5, 6
    #    3, 4, 6
    #  2 .     6
    # 
    ret = len(wall)
    table = collections.defaultdict(int)
    for i in range(len(wall)):
        presum = 0
        for j in range(len(wall[i]) - 1):  # - 1 to make sure we don't hash the end of the wall
            presum += wall[i][j]
            table[presum] += 1
            ret = min(ret, len(wall) - table[presum])
            
    return ret
            