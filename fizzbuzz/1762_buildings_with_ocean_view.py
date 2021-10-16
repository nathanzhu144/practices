# Nathan Zhu 10/16/2021 Bucktown, Chicago
# Leetcode 1762 | medium | actually easy
# Category: fizzbuzz
# 

def findBuildings(heights):
    """
    :type heights: List[int]
    :rtype: List[int]
    """
    # Notes:
    # all buildings to right have a smaller height to have an ocean
    # view.
    #
    # a building does not have an ocean view if any right neighbor
    # does not have an ocean view, and that neighbor's height is greater
    # or equal to that building's height
    #
    # iterate right to left
    
    N = len(heights)
    ret = []
    
    curr_max_right = float('-inf')
    for i in range(N - 1, -1, -1):
        # index i has ocean view
        if curr_max_right < heights[i]:
            ret.append(i)
            curr_max_right = heights[i]
    return ret[::-1]