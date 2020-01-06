# Nathan Zhu Monday 8:46 am, Starbucks
# Leetcode 755 | medium | medium
# Category: misc tricks
# Complexity N^2, where N is number of drops, and N is size of map.
#
def pourWater(heights, V, K):
    for i in range(V):
        curr = K
        
        while curr > 0 and heights[curr] >= heights[curr - 1]: curr -= 1
        while curr < len(heights) - 1 and heights[curr + 1] <= heights[curr]: curr += 1
        while curr > K and heights[curr] == heights[curr - 1]: curr -= 1
            
        heights[curr] += 1
        
    return heights